from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

from keywords_extracter_agent import extract_keywords
from reserach import search_pubmed


load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


prompt_template = ChatPromptTemplate.from_messages([
    ("system",
     "You are a research assistant. Given a problem statement and a list of grouped research paper summaries "
     "from different keywords, select and return the **top 5 most relevant papers** overall.\n"
     "Each paper has a title, abstract and url.\n\n"
     "Your goal:\n"
     "- Understand the core intent of the problem statement.\n" 
     "- Pick the 5 most useful and directly related papers your printing same matter more than 2 times make sure you print one time.\n\n"
     "summary should me an overviwe of the paper, not just a copy of the abstract. and it should have minimum 100 words\n"
     "Only return the top 5 papers in clean markdown format with **Title, Summary.**"),
    
    ("user", "Problem statement:\n{problem_statement}\n\nGrouped Papers:\n{grouped_papers}")
])

filter_chain = prompt_template | model


def format_papers_for_prompt(papers_by_keyword):
    combined = ""
    for keyword, papers in papers_by_keyword.items():
        combined += f"\nKeyword: {keyword}\n"
        for i, paper in enumerate(papers, 1):
            combined += f"{i}. Title: {paper['title']}\n   Summary: {paper['summary']}\n   URL: {paper['url']}\n\n"
    return combined


def filter_top_5_research_papers(problem_statement, papers_by_keyword):
    grouped_papers = format_papers_for_prompt(papers_by_keyword)
    response = filter_chain.invoke({
        "problem_statement": problem_statement,
        "grouped_papers": grouped_papers
    })
    return response.content


if __name__ == "__main__":
    print("Starting Literature Review Agent...")

    problem_statement = "Predicting prognosis and number of anti VEGF injections needed and visual acuity improvement in DME, CNVM based on OCT, Age, Vision, clinical risk factors."


    keywords = extract_keywords( problem_statement)
    papers_by_keyword = {}

    for keyword in keywords.split('\n'):
        if not keyword.strip():
            continue
            
        print(f"\n🔍 Searching for: {keyword.strip()}")
        papers = search_pubmed(keyword)
        papers_by_keyword[keyword.strip()] = papers
        #print(papers_by_keyword)

    top_papers = filter_top_5_research_papers(problem_statement, papers_by_keyword)
    #print(f"top_papers: {top_papers}")

    titles = []
    summaries = []
    for line in top_papers.splitlines():
        if "**Title:**" in line:
            title = line.split("**Title:**")[-1].strip()
            titles.append(title)
        elif "**Summary:**" in line:
            summary = line.split("**Summary:**")[-1].strip()
            summaries.append(summary)
    

print("\n✅ Final Extracted Top 5 Papers:\n")
for i, (title, summary) in enumerate(zip(titles, summaries), 1):
    print(f"\n🔖 Paper {i}")
    print("Title:", title)
    print("Summary:", summary)

    for paper in papers_by_keyword.values():
        for p in paper:
            if p['title'] == title:
                print("URL: 🔗", p['url'])  
                break
        
   


  

        
        

    