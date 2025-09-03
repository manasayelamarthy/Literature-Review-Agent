from google.adk.agents import Agent
from .sub_agents import literatureReview_agent


root_agent = Agent(
    name="mainAgent",
    model="gemini-2.0-flash",
    description="Acts as the entry point. Decides whether to run the Literature Review Agent or answer queries directly.",
    output_key="Manager_agent",
    instruction="""
You are the manager agent. Your role is to decide how to respond:

1. If the user provides a **project title** or asks for a **literature review**, then call the Literature Review Agent 
   (which includes introduction, research papers, analysis, research gaps, and conclusion).

   Example triggers:
   - "Generate a literature review on 'Predicting Disease Progression Using OCT Data'"
   - "I want a literature survey on deepfake detection"
   - "Direct project title"

2. Otherwise, behave like a **helpful assistant** and directly answer the user's query.

""",
    sub_agents=[literatureReview_agent]
)
