import json
import os

def export_to_json(tasks, path="data/tasks.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(tasks, f, indent=2)
    print(f"[EXPORT] tasks saved to {path}")