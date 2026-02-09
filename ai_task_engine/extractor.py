# extractor.py
import uuid
from schema import Task

def extract_tasks(raw_lines):
    tasks = []

    for line in raw_lines:
        task = Task(
            task_id=str(uuid.uuid4())[:8],
            name=line.strip(),
            owner="unassigned",
            domain="unknown",
            status="pending",
            priority="medium",
            dependency=None,
            risk="unknown"
        )
        tasks.append(task)

    return tasks