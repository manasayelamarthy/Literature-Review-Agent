from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

from arxiv import search_arxiv

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

promt = ChatPromptTemplate.from_messages([
    ("system",
        "You are a research assistant. Given a list of multiple research papers (titles, abstracts, and methods), your task is to analyze them collectively and extract high-level patterns across the literature.\n\n"
        "Specifically, identify and summarize the following aspects based on all the papers:\n"
        "-  Commonly used datasets (mention names, and whether they are public or private)\n"
        "-  Common model types or architectures (e.g., CNNs, RNNs, Transformers, etc.)\n"
        "-  Preprocessing or feature engineering methods used\n"
        "-  Validation techniques (e.g., k-fold, external test set, etc.)\n"
        "-  Whether the studies used public or private datasets\n\n"
        "Make sure to:\n"
        "- Use bullet points for clarity\n"
        "- Say 'Not reported' if a particular detail is missing\n"
        "- Avoid repeating the same points multiple times\n"
        "- Be concise but informative (no filler text)\n"
        "- Use markdown formatting"
        ),

    ("user", 
        "Here are the papers for analysis:\n{combined_paper_summaries}")

])

def analysis_agent(combined_paper_summaries):
    chat = promt | model
    result = chat.invoke({"combined_paper_summaries" : combined_paper_summaries})
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
    
    result = analysis_agent(summaries)  
    print(result)
    


