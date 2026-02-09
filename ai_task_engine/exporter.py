# exporter.py
import csv
import os

def export_to_csv(tasks, path="data/tasks.csv"):
    os.makedirs("data", exist_ok=True)

    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "task_id",
                "name",
                "owner",
                "domain",
                "status",
                "priority",
                "dependency",
                "risk"
            ]
        )
        writer.writeheader()
        for task in tasks:
            writer.writerow(task)

    print(f"[EXPORT] tasks saved to {path}")