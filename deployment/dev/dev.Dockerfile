FROM python:3.12-slim-bookworm

# Copy the pre-compiled uv binary from the installer stage to a directory in the final image's PATH
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set environment variables for optimal uv behavior
ENV UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=0


# Set working directory
WORKDIR /app

# update the alpine linux package index
RUN apt-get update
# for psutil, a dependencie of marimo.
# RUN apt-get install -y --no-install-recommends npm gcc
RUN rm -rf /var/lib/apt/lists/*

COPY uv.lock pyproject.toml ./
RUN uv sync --locked

# Configurar variáveis de ambiente
ENV PATH="/app/.venv/bin:$PATH"
ENV VIRTUAL_ENV="/app/.venv"
# Copy start bash script with the instruction on how to start Django.
COPY ./deployment/dev/start.sh /start.sh
# Convert Windows line endings (CRLF) to Unix (LF) if present and make the script executable
RUN sed -i 's/\r$//g' /start.sh && chmod +x /start.sh

# Default command - not used when running through docker compose
# as compose.yaml overrides this with the start.xsh script
CMD ["bash", "/start.sh"]