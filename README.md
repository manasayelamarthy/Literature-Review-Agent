# Literature-Review-Agent
## Literature Review Agent

This project is a **Literature Review Assistant** built using **Google’s Agent Development Kit (ADK)**.  
It provides a structured pipeline to generate a literature review from just a project title.  

The agent guides the process through:
- Collecting project details (title and scope)
- Searching for relevant research papers
- Summarizing and analyzing papers
- Identifying research gaps
- Producing a final conclusion and structured literature review

---

## Live Deployment

You can directly try the deployed agent here:  
👉 [Literature Review Agent (Cloud Run Deployment)](https://literature-agent-service-809404788066.asia-south1.run.app)

---

## Features

- Modular agent pipeline using Google ADK
- Automatic research paper retrieval and filtering
- Paper summaries with datasets, methods, results, and limitations
- Gap analysis and conclusion generation
- Deployable to **Google Cloud Run** with Web UI or CLI

---

## Setup & Requirements

- Python 3.10+  
- Google ADK installed (`pip install google-genai[adk]`)  
- Docker and gcloud CLI installed (for deployment to Cloud Run)  
- Google API key from AI Studio (or Vertex AI access)  

Clone the repository:
```bash
git clone https://github.com/manasayelamarthy/Literature-Review-Agent.git
cd Literature-Review-Agent/Google_adk
```
## Resources :

https://google.github.io/adk-docs/
