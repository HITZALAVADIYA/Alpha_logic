from crewai import Agent

def get_normalizer(llm_obj):
    return Agent(
        role='Skill Taxonomy Expert',
        goal='Map raw resume skills to industry standard terms.',
        backstory='You ensure that "K8s" is recognized as "Kubernetes" for better matching.',
        llm=llm_obj,
        verbose=True,
        allow_delegation=False
    )