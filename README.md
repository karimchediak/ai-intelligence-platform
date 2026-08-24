# AegisAI — Autonomous Intelligence Platform

Production-style AI research platform combining agents, retrieval, ML, anomaly detection, evaluation, APIs and observability.

## Architecture
Ingestion → Retrieval → Agents → ML → Evaluation → API → UI

## Run
`pip install -r requirements.txt`

`uvicorn backend.api:app --reload`

`streamlit run frontend/app.py`
