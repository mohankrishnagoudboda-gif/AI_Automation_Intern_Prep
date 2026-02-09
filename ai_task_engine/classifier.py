# classifier.py

def classify_domain(task_name):
    name = task_name.lower()

    if "hr" in name or "onboard" in name:
        return "HR"
    if "it" in name or "access" in name or "laptop" in name:
        return "IT"
    if "finance" in name or "cfo" in name or "approval" in name:
        return "Finance"
    if "legal" in name or "contract" in name or "signature" in name:
        return "Legal"
    if "security" in name or "audit" in name:
        return "Security"

    return "General"