
from google.adk.agents import Agent
import requests
import feedparser

def search_arxiv(query: str):
    """
    Searches the arXiv API for papers matching the given query and returns a list of paper details.
    Args:
        query (str): The search query string to use for finding relevant papers on arXiv.
    Returns:
        list of dict: A list of dictionaries, each containing information about a paper:
            - title (str): The title of the paper.
            - authors (list of str): The names of the authors.
            - summary (str): The abstract or summary of the paper.
            - published (str): The publication date of the paper.
            - link (str): The URL to the paper's arXiv page.
            - pdf_url (str or None): The direct URL to the PDF of the paper, or None if not available.
    """

    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=5"

    response = requests.get(url)
    feed = feedparser.parse(response.text)

    papers = []
    for entry in feed.entries:
        paper = {
            "title" : entry.title,
            "authors": [author.name for author in entry.authors],
            "summary": entry.summary,
            "published": entry.published,
            "link": entry.link,
            "pdf_url": next((l.href for l in entry.links if l.type == "application/pdf"), None)
        }
        papers.append(paper)

    return papers



research_agent = Agent(
    name="SearchPapersAgent",
    model="gemini-2.0-flash",
    description="Fetches recent related research papers from arXiv.",
    output_key="paper_search_results",
    tools=[search_arxiv],
    instruction="""
You are research agent.
Your task is to search arXiv using the provided research topic and return a concise list of **relevant research papers**.
From the given introduction text, identify the 'Project Title' and
use it to search for the most relevant and recent research papers.

**introduction:**
    ```
    {literature_review_intro}
    ```

Steps:
- Use the `search_arxiv` tool to fetch research papers.
- The input will be a research topic or project title (as `query`).
- Return a **summary of each paper**, including:
  - Title
  - Authors - give not more than 3
  - Give full Summary that is provided not small,minimum 10 lines is needed 
  - Published date
  - Link to the paper

Format your response cleanly with paper-wise sections and short summaries.
"""
)