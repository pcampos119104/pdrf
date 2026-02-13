# List all just commands
default:
    just --list

# Build the docker image
runlocal:
    uv run uvicorn pdrf.main:app --host 0.0.0.0 --port 8000 --reload
# Build the docker image
build:
    docker compose build

# Run the Django app and dependecies services in development mode
up:
    docker compose up -d

# Stop all the containers
down:
    docker compose down

# Enter in the container shell
shell:
    docker compose run --rm app bash