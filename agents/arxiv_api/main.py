from Intro import intro
from arxiv import search_arxiv
from analysis import analysis_agent
from analysis import combine_summaries
from research_gap import research_gap_agent
from conclusion import conclusion_agent

if __name__ == "__main__":
    topic = "Predicting prognosis and number of anti VEGF injections needed and visual acuity improvement in DME, CNVM based on OCT, Age, Vision, clinical risk factors."
    
    introduction = intro(topic)
    print(introduction)

    extract_papers = search_arxiv(topic)
    for paper in extract_papers:
            print(f" Title: {paper['title']}")
            print(f" Authors: {', '.join(paper['authors'])}")
            print(f" Published: {paper['published']}")
            print(f" PDF: {paper['pdf_url']}")
            print(f" Summary: {paper['summary']}\n")

    summaries = combine_summaries(query = topic)
    analysis = analysis_agent(summaries)
    print(analysis)

    research_gap = research_gap_agent(summaries)
    print(research_gap)

    conclusion = conclusion_agent(summaries, research_gap)
    print(conclusion)

    