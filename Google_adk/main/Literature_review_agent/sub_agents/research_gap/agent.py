from google.adk.agents import Agent


researchGap_agent = Agent(
    name="ResearchGap",
    model="gemini-2.0-flash",
    description="Finds the top 5 research gaps from multiple paper summaries.",
    output_key="research_gaps",
    instruction = """
    You are a research assistant. extract summaries from the given tool  and give research gaps from those 
    Below is the data of the arxiv papers 

     **papers to get research_gap details:**
    ```
    {paper_search_results}
    ```

    Focus especially on:
    - Lack of generalization to real-world or unseen data
    - Limited datasets (small size, private, single-institution)
    - Outdated models or missing recent advances
    - Missing ablation studies or interpretability
    - No external validation or comparison with state-of-the-art

    Guidelines:
    - Present gaps as bullet points
    - Keep the language simple, clear, and under 100 words total
    - Avoid vague or filler phrases
    - Use markdown formatting for clarity
    """,
    
)