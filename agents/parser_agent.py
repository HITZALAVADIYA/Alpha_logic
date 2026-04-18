# agents/parser_agent.py (aur baaki 3 files mein bhi same change)
from crewai import Agent

def get_parser(llm_obj): # llm_val yahan "groq/mixtral..." wali string hogi
    return Agent(
        role='Data Extraction Specialist',
        goal='Extract technical data.',
        backstory='Expert resume parser.',
        llm=llm_obj, # ✅ CrewAI ab is string ko dekh kar 'groq' provider khud dhundh lega
        verbose=True,
        allow_delegation=False
    )