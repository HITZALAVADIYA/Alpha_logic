from crewai import Agent

def get_generator(llm_obj):
    return Agent(
        role='Communication Expert & Recruiter Specialist',
        goal='Draft a perfect personalized cover letter for the candidate and a cold email for the recruiter in a strictly structured JSON format.',
        backstory='Expert in tech recruitment communications, writing personalized persuasive cover letters and clear, decisive acceptance/rejection emails.',
        llm=llm_obj,
        verbose=True,
        allow_delegation=False
    )
