from crewai import Agent

def get_inquisitor(llm_obj):
    return Agent(
        role='Technical Interviewer',
        goal='Generate 3 high-impact technical questions for the candidate.',
        backstory='Senior Lead Developer who tests if the candidate actually knows what they wrote.',
        llm=llm_obj,
        verbose=True,
        allow_delegation=False
    )