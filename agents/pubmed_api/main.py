from keywords_extracter_agent import extract_keywords
from reserach import search_pubmed
from Filtering_agent import filter_top_5_research_papers
from summarize_agent import get_full_text_url, download_and_extract_pdf, summarize_text

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
    

    top_papers = filter_top_5_research_papers(problem_statement, papers_by_keyword)
    print(top_papers)

    pubmed_links = [
        paper["url"] for paper in top_papers
        if isinstance(paper, dict) and paper.get("url") and paper["url"] != "N/A"
    ]


    for url in pubmed_links:
        full_text_url = get_full_text_url(url)
        if full_text_url:
            print(f"Downloading from: {full_text_url}")
            paper_text = download_and_extract_pdf(full_text_url)
            summary = summarize_text(paper_text)
            print("Summary:\n", summary)
        else:
            print(f"Full text not available or paywalled for: {url}")