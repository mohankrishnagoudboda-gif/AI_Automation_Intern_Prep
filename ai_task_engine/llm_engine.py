# llm_engine.py
import json
import subprocess

def llm_enrich(task_name):
    prompt = f"""
You are an AI project automation system.

Classify this task:
"{task_name}"

Return JSON only with fields:
domain, priority, risk, dependency

Rules:
- domain: HR, IT, Finance, Legal, Security, Operations
- priority: low, medium, high
- risk: low, medium, high
- dependency: short text or null
"""

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True
    )

    try:
        return json.loads(result.stdout)
    except:
        return {
            "domain": "unknown",
            "priority": "medium",
            "risk": "unknown",
            "dependency": None
        }