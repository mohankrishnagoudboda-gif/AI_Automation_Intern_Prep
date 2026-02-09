from extractor import extract_tasks
from classifier import classify_domain
from risks import assess_risk
from exporter import export_to_csv
from export_json import export_to_json
from llm_engine import llm_enrich
import argparse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", default="data/raw_notes.txt")
parser.add_argument("--format", default="csv", choices=["csv", "json"])
args = parser.parse_args()

# Load raw notes
with open(args.input, "r") as f:
    raw_lines = f.readlines()

# Extract tasks
tasks = extract_tasks(raw_lines)

# Classify + assess risk
structured = []
for task in tasks:
    ai_data = llm_enrich(task.name)

    task.domain = ai_data["domain"]
    task.priority = ai_data["priority"]
    task.risk = ai_data["risk"]
    task.dependency = ai_data["dependency"]

    structured.append(task.to_dict())
# Export
if args.format == "csv":
    export_to_csv(structured)
elif args.format == "json":
    export_to_json(structured)

print(f"Pipeline complete. Data exported as {args.format}")