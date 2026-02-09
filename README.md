# AI Automation Engine – M&A Integration Prototype

## Purpose
Internal automation system for structuring unstructured integration data during M&A workflows.

## Features
- Unstructured text ingestion
- Task extraction
- Domain classification
- Risk assessment
- AI enrichment (LLM)
- CSV export
- JSON export
- CLI interface
- Modular pipeline architecture

## Run
```bash
python3 run_engine.py --format csv
python3 run_engine.py --format json
Pipeline:
Ingest → Extract → Classify → Enrich → Risk → Export
