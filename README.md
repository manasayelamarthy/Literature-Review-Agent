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


## Quick start – Google ADK (with local Web UI or CLI)
1) Create and activate a virtual environment
   
    ```sh
     python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

    macOS/Linux
   ```sh
    python -m venv venv
    source venv/bin/activate
    ```

2) Install dependencies
    ```sh
    pip install -r Google_adk/requirements.txt
    ```
3) Set environment variables
   ```sh
   GOOGLE_API_KEY = "<your-google-ai-studio-api-key>"
   ```
4) Run the ADK Web UI\

   From the project root:
     ```sh
      adk web or adk run
     ```

### Steps:
1. The command starts a local FastAPI server and the ADK dev UI.\
2. The terminal will print a local URL (commonly http://localhost:8000). Open it in your browser.\
3. In the UI:Select the agent if prompted (there should be a single root_agent).\
4. Start by sending a greeting and then provide your project title when asked.\
5. The main agent will request the title first; once provided, it orchestrates the sequential sub-agents.\

## Quick start – LangChain 
1) Create and activate a virtual environment
   
    ```sh
     python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

    macOS/Linux
   ```sh
    python -m venv venv
    source venv/bin/activate
    ```

2) Install dependencies
    ```sh
    pip install -r Google_adk/requirements.txt
    ```
3) Set environment variables
   ```sh
   GOOGLE_API_KEY = "<your-google-ai-studio-api-key>"
   ```
4) Run
   ```sh
   python run main.py
   ```

### How to use the agent effectively
> Start with a short greeting, then provide your project title/topic\
> The pipeline proceeds in order:\
      1.Introduction/background\
      2.Paper search on arXiv and detailed summaries\
      3.Cross-paper analysis (datasets, models, preprocessing, validation, data access)\
      4.Research gaps\
      5.Conclusion and recommended next steps\
> The research agent uses the arXiv API. You can tune max_results or query terms in its tool code if you need more or fewer papers.


## Configuration notes
 **Model**: The ADK and LangChain flows are configured to use Gemini models. You can switch models by updating the model argument in the agent definitions.\
**Search tool**: The arXiv search tool is defined in the research agent. Edit max_results or query composition there.\
**Ordering**: The orchestrator ensures the title is collected first, and only then runs the sub-agents sequentially.

## Acknowledgments
  1. Google Agent Development Kit (ADK).\
  2. LangChain.\
  3. arXiv API.\
  4. pubmed_api






