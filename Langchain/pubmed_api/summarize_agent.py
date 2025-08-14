import requests
from bs4 import BeautifulSoup
import fitz  
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def get_full_text_url(pubmed_url):
    response = requests.get(pubmed_url)
    soup = BeautifulSoup(response.content, "html.parser") 
   
    full_text_section = soup.find("div", {"class": "full-text-links-list"})
    if full_text_section:
        links = full_text_section.find_all("a")
        for link in links:
            href = link.get("href")
            if href and ("pdf" in href or "full" in href):
                return href
    return None


def download_and_extract_pdf(pdf_url, save_path="paper.pdf"):
    response = requests.get(pdf_url)
    with open(save_path, "wb") as f:
        f.write(response.content)

    # Extract text
    doc = fitz.open(save_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

def summarize_text(text):
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You're a scientific researcher. Summarize the following academic paper text into a structured abstract: Background, Methods, Results, and Conclusion."),
        ("user", "{text}")
    ])
    chain = prompt | model
    return chain.invoke({"text": text}).content


