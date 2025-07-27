from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

from arxiv import search_arxiv

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

promt_template = ChatPromptTemplate([
    ("system",
        "You are a research assistant. Given summaries of multiple research papers (including their methods, datasets, results, and limitations), your task is to identify the key **research gaps** in the current literature.\n\n"
        "Specifically, analyze the papers and extract what's missing, underexplored, or could be improved in future work. Look for things like:\n"
        "-  Lack of generalization to real-world or unseen data\n"
        "-  Limited datasets (e.g., small size, private, or single-institution)\n"
        "-  Absence of ablation studies or interpretability\n"
        "-  No comparison with state-of-the-art methods\n"
        "-  Outdated models (e.g., not using transformers or recent advances)\n"
        "-  Evaluation only on internal validation, no external test\n\n"
        "Make sure to:\n"
        "- Present each research gap clearly using bullet points\n"
        "- Keep the language concise but insightful\n"
        "- Avoid vague or generic gaps like 'more data needed' unless it’s strongly evident\n"
        "- Use markdown formatting for readability"
        "give top 5 research gaps from all of these summaries"
        "do go beyond the point reserch gap mainly should focus of oudated model or about dataset or any important topics"
        "And reduce the matter to below 100 words or less convey the whole point using less number of words and use easy language not complex terms"
),      

    ("user",
        "Here are the research paper summaries:\n{combined_paper_summaries}")

])

def research_gap_agent(combined_paper_summaries):
    chat = promt_template | model
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
    
    result = research_gap_agent(summaries)  
    print(result)
    


