# List all just commands
default:
    just --list

# Build the docker image
run t:
    uv run uvicorn pdrf.main:app --host 0.0.0.0 --port 8000 --reload