from google.adk.agents import Agent

introduction_agent = Agent(
    model = "gemini-2.0-flash",
    name = "introduction_agent",
    instruction = """
    "You are an expert research assistant. Your task is to write a **concise and professional introduction** for a literature review "
     "based on a given research topic or project title.\n\n"

    "Output should be in this format :\n"

    Title of the project : given by the user
    
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
     "Write in paragraph form. Do NOT return bullet points or lists.
     Each must not contain more than 4 lines

    """,
     description="Generates a professional literature review introduction based on the given project title.",
     output_key="literature_review_intro"
)



