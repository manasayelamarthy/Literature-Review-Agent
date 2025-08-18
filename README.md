# Literature-Review-Agent

### Literature-Review-Agent

A multi-agent pipeline that drafts a literature review from a user-provided project title/topic.
Two runnable implementations are included:
1.Google ADK (Agent Development Kit) – with a local web UI or CLI.\
2.LangChain – simple script execution from the terminal.

The pipeline orchestrates the following sub-agents:
> Introduction agent – writes a concise introduction/background.\
> Research agent – searches arXiv and summarizes papers.\
> Analysis agent – extracts common datasets, models, preprocessing, validation.\
> Research-gap agent – identifies gaps and limitations.\
> Conclusion agent – synthesizes findings and next steps.

Deployment to Cloud Run is not included yet; this README focuses on running locally.

## Prerequisites
1.Python 3.10+ (recommended 3.11).\
2.A terminal with basic build tools.\
3.An API key for Google Generative AI (Gemini). You can use AI Studio.\
4.Create an API key and keep it handy.\
Cloud SDK and Docker are not required for local runs.
