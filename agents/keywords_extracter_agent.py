from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")  

prompt_template = ChatPromptTemplate.from_messages([
    ("system", 
     "You are an intelligent research assistant working on building a literature review agent. "
     "Your task is to extract **top 5 complete, meaningful search phrases ** from the given research topic. "
     "These phrases will be used to search for academic papers in tools like Semantic Scholar or arXiv.\n\n"
     " Each phrase should be:\n"
     "- Specific and informative\n"
     "- 5 to 15 words long\n"
     "- Contain no incomplete terms\n"
     "- Sound like a research paper title or academic query\n"
     "- Avoid generic words alone (like just 'AI', 'models', 'data')\n\n"
     "Do NOT return single words or broken short phrases.\n"
     " Avoid repetition or overlapping meanings.\n\n"
     "Return only a comma-separated list of meaningful research phrases."
    ),
    ("user", "Extract important research keywords from the following topic: {topic}")
])

def extract_keywords(topic):
    """Extracts keywords from a given research topic using a language model."""
    chain = prompt_template | model
    result = chain.invoke({"topic": topic})
    return result.content

#if __name__ == "__main__":
    #topic = "Predicting Disease Progression Using OCT Data. " \
    #"Predicting prognosis and number of anti VEGF injections needed and visual acuity improvement" \
  #  "  in DME, CNVM  based on OCT , Age ,Vision, clinical risk factors."
   # keywords = extract_keywords(topic)
    #print("Extracted Keywords:", keywords)
    
   
    #keywords_list = [kw.strip() for kw in keywords.split(",") if kw.strip()]
    #print("Keywords List:", keywords_list)