from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

from arxiv import search_arxiv
from research_gap import research_gap_agent

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

prompt = ChatPromptTemplate.from_messages([
    ("system",
        "You are a helpful research assistant. Your job is to write a short and simple conclusion for a literature review.\n\n"
        "Given a summary of related research papers and identified research gaps, generate:\n"
        "1. A plain-language summary of what the papers overall found.\n"
        "2. A clear mention of the gaps that still exist.\n"
        "3. A brief statement about how the new project will fill these gaps.\n"
        "4. A recommended best approach to do this project based on the existing literature.\n\n"
        "Your explanation should be easy to read, avoid complex words, and be no longer than 2-3 short paragraphs."
        "dont add statements that ask user to fill the gaps"
    ),


    ("user",
        "Here is the summary of the literature:\n\n{combined_paper_summaries}\n\n"
        "And here are the research gaps identified:\n\n{research_gaps}\n\n"
        "Now write a simple conclusion and recommend the best method to carry out the project effectively."
    )

])

def conclusion_agent(combined_paper_summaries, research_gap):
    chat = prompt | model
    result = chat.invoke({
        "combined_paper_summaries": combined_paper_summaries,
        "research_gaps": research_gap
    })
    return result.content


def combine_summaries(query):
    results = search_arxiv(query)

    combined_paper_summaries = ''

    for i, paper in enumerate(results):
        combined_paper_summaries += f"{i}. Title: {paper['title']}\n   Summary: {paper['summary']}\n  "
    return combined_paper_summaries


if __name__ == "__main__":
    query = "Predicting Disease Progression Using OCT Data and Predicting prognosis and number of anti VEGF injections needed and visual acuity improvement in DME, CNVM based on OCT, Age, Vision, clinical risk factors."

    summaries = combine_summaries(query)
    reseach_gap = research_gap_agent(summaries)
    
    result = conclusion_agent(summaries, reseach_gap)  
    print(result)
    


