import requests
import feedparser



def search_arxiv(query):
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


if __name__ == "__main__":

    query = "Predicting Disease Progression Using OCT Data and Predicting prognosis and number of anti VEGF injections needed and visual acuity improvement in DME, CNVM based on OCT, Age, Vision, clinical risk factors."

    results = search_arxiv(query)

    for paper in results:
            print(f" Title: {paper['title']}")
            print(f" Authors: {', '.join(paper['authors'])}")
            print(f" Published: {paper['published']}")
            print(f" PDF: {paper['pdf_url']}")
            print(f" Summary: {paper['summary']}\n")
