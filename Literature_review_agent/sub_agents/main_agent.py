
from google.adk.agents import SequentialAgent

from .Introduction_agent import introduction_agent
from .research_agent import research_agent
from .analysis_agent import analysis_agent
from .researchgap_agent import researchGap_agent
from .Conclusion_agent import conclusion_agent


literatureReview_agent = SequentialAgent(
    name="LiteratureReviewAgent",
    sub_agents=[
        introduction_agent,
        research_agent,
        analysis_agent,
        researchGap_agent,
        conclusion_agent
    ],
    description=(
        "Executes a literature review pipeline :, "
         "According to  the below order:"
        "1. Introduction,"
        "2.paper search,"
        "3. anaylsis, "
        "4.research gap identification, "
        "5. conclusion."
    ),
)

