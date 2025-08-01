import requests
import xml.etree.ElementTree as ET
import os
from dotenv import load_dotenv
from keywords_extracter_agent import extract_keywords

load_dotenv()

def search_pubmed(keywords, max_results=5):
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    api_key = os.getenv("PUBMED_API_KEY")

    search_terms = keywords.split('\n')[0] 
    search_query = search_terms.strip().replace(',', ' AND ')

    search = requests.get(
        f"{base}esearch.fcgi?db=pubmed&retmode=json&retmax={max_results}&term={search_query}&api_key={api_key}"
    )

    try:
        search_json = search.json()
    except requests.exceptions.JSONDecodeError:
        return []

    ids = ",".join(search_json.get("esearchresult", {}).get("idlist", []))
    if not ids:
        return []

    fetch = requests.get(
        f"{base}efetch.fcgi?db=pubmed&retmode=xml&id={ids}&api_key={api_key}"
    )
    
    root = ET.fromstring(fetch.content)
    results = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.find(".//PMID").text
        title = article.find(".//ArticleTitle").text
        abstract_elem = article.find(".//AbstractText")
        abstract = abstract_elem.text if abstract_elem is not None else "No abstract available"
        pubmed_url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
        
        results.append({
            "title": title, 
            "summary": abstract,
            "url": pubmed_url
        })

    return results

if __name__ == "__main__":
    keywords = extract_keywords(
        "Predicting Disease Progression Using OCT Data. "
        "Predicting prognosis and number of anti VEGF injections needed and visual acuity improvement "
        "in DME, CNVM based on OCT, Age, Vision, clinical risk factors."
    )

    for keyword in keywords.split('\n'):
        if not keyword.strip():
            continue
            
        print(f"\n🔍 Searching for: {keyword.strip()}")
        papers = search_pubmed(keyword)
        
        if papers:
            print(f"\nFound {len(papers)} papers:")
            for i, paper in enumerate(papers, 1):
                print(f"\n🔖 Paper {i}")
                print("Title:", paper["title"])
                print("Abstract:", paper["summary"])
                print("URL: 🔗", paper["url"])  
        else:
            print("No papers found for this keyword")
            print("Retrying with a different keyword...")
            papers = search_pubmed(keyword)
            for i, paper in enumerate(papers, 1):
                print(f"\n🔖 Paper {i}")
                print("Title:", paper["title"])
                print("Abstract:", paper["summary"])
                print("URLs: 🔗", paper["url"])


    