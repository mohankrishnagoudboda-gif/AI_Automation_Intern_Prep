# risks.py

def assess_risk(task):
    if "delayed" in task.name.lower():
        return "high"

    if task.status == "blocked":
        return "high"

    if task.priority == "high":
        return "medium"

    return "low"