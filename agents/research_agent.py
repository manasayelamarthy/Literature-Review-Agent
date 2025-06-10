import requests


def search_semantic_scholar(keywords, limit=5):
    query = "+".join(keywords.split())
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit={limit}&fields=title,authors,url,abstract,year,isOpenAccess,externalIds"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        papers = response.json().get("data", [])
        results = []
        for paper in papers:
            pdf_url = None
            if paper.get("isOpenAccess") and "arXiv" in paper.get("externalIds", {}):
                arxiv_id = paper["externalIds"]["arXiv"]
                pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
            results.append({
                "title": paper["title"],
                "authors": ", ".join([a["name"] for a in paper["authors"]]),
                "abstract": paper.get("abstract", "No abstract found."),
                "year": paper.get("year"),
                "url": paper.get("url"),
                "pdf_url": pdf_url
            })
        return results
    else:
        raise Exception(f"Failed to fetch papers: {response.status_code}")



keywords = "deep learning in medical imaging"
papers = search_semantic_scholar(keywords)

for i, paper in enumerate(papers, 1):
    print(f"\n🔖 Paper {i}")
    print("Title:", paper["title"])
    print("Authors:", paper["authors"])
    print("Year:", paper["year"])
    print("Abstract:", paper["abstract"])
    print("URL:", paper["url"])
    print("PDF URL:", paper["pdf_url"])
