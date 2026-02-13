#!/usr/bin/env bash
# start.sh - Development startup script for the FastAPI application

# Fail fast:
# -e  : exit immediately if a command exits with non-zero status
# -o pipefail : fail if any command in a pipeline fails
set -euo pipefail

# Log unexpected errors (similar à $XONSH_TRACEBACK_LOGFILE)
trap 'echo "Error on line $LINENO" >> /tmp/bash_traceback.log' ERR

echo "Starting Marimo"

# Run marimo in edit mode:
# --host 0.0.0.0  : accessible from any network interface
# -p 2718         : port 2718
# --no-token      : disable authentication token
# --headless      : do not open browser
# Redirect stdout/stderr to /dev/null and run in background
# marimo edit --host 0.0.0.0 -p 2718 --no-token --headless > /dev/null 2>&1 &

echo "Starting fastapi server..."

# Run FastAPI (foreground process)
exec uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
