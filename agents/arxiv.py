import requests
import feedparser

query = "Predicting Disease Progression Using OCT Data and Predicting prognosis and number of anti VEGF injections needed and visual acuity improvement in DME, CNVM based on OCT, Age, Vision, clinical risk factors."

url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=5"

response = requests.get(url)
feed = feedparser.parse(response.text)

for entry in feed.entries:
    print(f"Title: {entry.title}")
    print(f"Authors: {[author.name for author in entry.authors]}")
    print(f"Published: {entry.published}")
    print(f"Summary: {entry.summary}")  
    print(f"Link: {entry.link}")
    print("-" * 80)
