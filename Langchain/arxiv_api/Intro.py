from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash") 

prompt_template = ChatPromptTemplate.from_messages([
    ("system", 
     "You are an expert research assistant. Your task is to write a **concise and professional introduction** for a literature review "
     "based on a given research topic or project title.\n\n"

    "Output should be in this format :\n"
    
     "Introduction / Background:\n"
     "– Briefly explain the topic in 3–4 sentences.\n"
     "– Clearly mention the **research domain**, **key technologies involved**, and **clinical or technical relevance**.\n\n"

     "Why Is This Important?\n"
     "– Describe the **real-world significance** of the topic.\n"
     "– Mention clinical impact, technical importance, or societal relevance.\n\n"

     "Goal of the Literature Review:\n"
     "– Clearly state the **objective of reviewing existing literature**.\n"
     "– Example: 'To understand current approaches for ___ and identify research gaps to guide future work.'\n\n"

     " Output Format:\n"
     "Write in paragraph form. Do NOT return bullet points or lists."
    ),
    ("user", "Generate an introduction for the following topic: {topic}")
])



def intro(topic):
    chain = prompt_template| model
    result = chain.invoke({"topic": topic})
    return result.content



if __name__ == "__main__":
    topic = "Predicting prognosis and number of anti VEGF injections needed and visual acuity improvement in DME, CNVM based on OCT, Age, Vision, clinical risk factors."
    results = intro(topic)
    print(results)
