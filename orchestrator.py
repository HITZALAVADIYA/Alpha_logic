import os
import json
import re
import concurrent.futures
from crewai import Agent, Task, Crew, Process, LLM
from agents.parser_agent import get_parser
from agents.normalizer_agent import get_normalizer
from agents.matcher_agent import get_matcher
from agents.inquisitor_agent import get_inquisitor
from agents.generator_agent import get_generator

# --- API KEY ---


# 🔥 OPTIMIZATION: Model ko global rakha hai taaki har loop mein naya object na bane
# Groq ka sabse naya aur fast model use kiya hai
# Purana Groq wala LLM hata kar ye daalo
# orchestrator.py
from crewai import LLM
import os

# Ye line zaroori hai LiteLLM ke liye
# orchestrator.py
from crewai import LLM

sentinel_llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key="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", 
    temperature=0 
)
def _run_crew(resume_text, jd_text):
    """Core logic for a single resume analysis"""
    # Agents Initialization
    p_agent = get_parser(sentinel_llm)      
    n_agent = get_normalizer(sentinel_llm)  
    m_agent = get_matcher(sentinel_llm)     
    i_agent = get_inquisitor(sentinel_llm)
    g_agent = get_generator(sentinel_llm)

    # --- Task Pipeline ---
    task1 = Task(
        description=f"Extract structured technical skills and experience from: {resume_text}",
        expected_output="Structured summary of skills.",
        agent=p_agent
    )

    task2 = Task(
        description=f"Normalize skills against JD requirements: {jd_text}",
        expected_output="Normalized skill list.",
        agent=n_agent,
        context=[task1]
    )

    task3 = Task(
        description=f"Compare profile vs JD: {jd_text}. Scoring: 0-100.",
        expected_output="Match score and brief insight.",
        agent=m_agent,
        context=[task2]
    )

    task4 = Task(
        description="Identify gaps and generate 3 critical technical interview questions.",
        expected_output="List of questions and gaps identified.",
        agent=i_agent,
        context=[task3]
    )

    task5 = Task(
        description=(
            "Based on the analysis, draft a personalized Cover Letter for the candidate to apply for this job. "
            "ALSO draft a Cold Email for the recruiter (Acceptance if match score > 75%, else Rejection). "
            "OUTPUT ONLY RAW JSON. No markdown tags. "
            'Format MUST BE EXACTLY: {"score": 85, "skills": ["..."], "insight": "...", "questions": ["..."], "cover_letter": "...", "cold_email": "..."}'
        ),
        expected_output="Raw JSON string only.",
        agent=g_agent,
        context=[task3, task4]
    )

    # Sequential process for deep analysis
    sentinel_crew = Crew(
        agents=[p_agent, n_agent, m_agent, i_agent, g_agent],
        tasks=[task1, task2, task3, task4, task5],
        process=Process.sequential,
        verbose=False # Bulk mein True rakhoge toh terminal bhar jayega
    )
    
    return sentinel_crew.kickoff()

def run_sentinel_analysis(resume_text, jd_text):
    """
    EntryPoint for app.py. 
    Kyunki app.py ab loop mein call kar raha hai, 
    humne isey thread-safe banaya hai.
    """
    max_retries = 2
    for attempt in range(max_retries + 1):
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(_run_crew, resume_text, jd_text)
                return future.result(timeout=180) # Increansed timeout to 180s for heavy batches
                
        except Exception as e:
            err_str = str(e)
            print(f"❌ Orchestrator Error (Attempt {attempt+1}): {err_str}")
            
            if ("RateLimitError" in err_str or "rate_limit_exceeded" in err_str or "429" in err_str) and attempt < max_retries:
                import time
                print(f"⏳ Groq Free Tier Rolling Window hit. Waiting 21 seconds to flush tokens...")
                time.sleep(21)
                continue # Retry!
                
            # Default JSON return taaki app.py crash na ho
            return json.dumps({
                "score": 0, 
                "skills": ["Error Encountered"], 
                "insight": f"System Alert: {err_str[:50]}...", 
                "questions": ["Please try scanning this file again."],
                "cover_letter": "System Error: Failed to generate due to strict API rate limits.",
                "cold_email": "System Error: Failed to generate due to strict API rate limits."
            })