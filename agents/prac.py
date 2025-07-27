from dotenv import load_dotenv
import os
import requests

load_dotenv()

def search_pubmed(Keywords, max_results = 5):
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    api_key = os.getenv("PUBMED_API_KEY")

    search_keywords = Keywords.split("\n")[0]
    search_query = search_keywords.strip().replace(',' , 'AND')

    search = requests.get(
        f"{base}esearch.fcgi?db=pubmed&retmode=json&retmax={max_results}&term={search_query}&api_key={api_key}"
    )

    