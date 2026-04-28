# AGENTS.md

## Project Overview
- Python project using CrewAI Flow for recipe processing
- FastAPI REST API for unstructured recipe text and PDF processing
- Dependencies managed with UV
- Main package: `core.pdrf`
- Ollama required for LLM (llama3.1:8b model)

## Key Commands
- Install deps: `uv sync`
- Run API server: `uv run uvicorn api.main:app --reload`
- Run flow directly: `python -c "from core.pdrf.pdr_flow import PdrFlow; f = PdrFlow(); f.kickoff(inputs={'raw_recipe': 'recipe text'})"`

## API Endpoints
- `GET /` - Root
- `GET /health` - Health check
- `POST /recipes/process/unstructured` - Process text recipe
- `POST /recipes/process/pdf` - Process PDF recipe (uses marker-pdf)

## Structure
- Flow: `core/pdrf/pdr_flow.py` (PdrFlow class)
- Crew: `core/pdrf/crews/pdr/crew.py` (PdrCrew class)
- Configs: `core/pdrf/crews/pdr/config/agents.yaml`, `tasks.yaml`
- API: `api/main.py`

## Setup Notes
- Requires Ollama running with llama3.1:8b
- No linting/formatting configured yet
- No tests implemented

This document should be updated as the project evolves. For questions, refer to CrewAI docs or project issues.