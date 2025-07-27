import requests
import feedparser
from keywords_extracter_agent import extract_keywords

def search_arXiv(keyword, max_results = 5, start_index = 0, category = None):
    if category:
        search_query = f"cat:{category}+AND+all:{keyword.replace(' ', '+')}"
    else:
        search_query = f"all:{keyword.replace(' ','+')}"

    base_url = "http://export.arxiv.org/api/query"

    params = {
    "search_query": search_query,
    "start": start_index,
    "max_results": max_results,
    "sortBy": "submittedDate",
    "sortOrder": "descending"
    }

    response = requests.get(base_url, params = params)
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

if __name__ == "__main__":
    #keyword = "Predicting Disease Progression Using OCT Data and Predicting prognosis and number of anti VEGF injections needed and visual acuity improvement in DME, CNVM based on OCT, Age, Vision, clinical risk factors."
    keyword = "machine learning"
            
    print(f"\n🔍 Searching for: {keyword.strip()}")
    results = search_arXiv(keyword, max_results=3)

    for paper in results:
        print(f"📄 Title: {paper['title']}")
        print(f"✍️  Authors: {', '.join(paper['authors'])}")
        print(f"📅 Published: {paper['published']}")
        print(f"🔗 PDF: {paper['pdf_url']}")
        print(f"📝 Summary: {paper['summary'][:300]}...\n")



