from crewai import Agent

def get_matcher(llm_val):
    return Agent(
        role='Executive Decision Maker',
        goal='Assign a definitive match percentage. Be extremely strict.',
        backstory='You are a world-class recruiter who gives 100% only to perfect candidates.',
        llm=llm_val,
        verbose=True,
        allow_delegation=False
    )