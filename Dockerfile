# Build stage: Use a full Python image for installing dependencies
FROM python:3.13-slim-bookworm AS builder

# Set the working directory
WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.9.2 /uv /uvx /bin/

# Copy dependency files
COPY pyproject.toml uv.lock .python-version ./

# Install dependencies without dev packages or cache
RUN uv sync --no-dev --no-cache --locked

# Runtime stage: Use a minimal image
FROM python:3.13-slim-bookworm

# Set the working directory
WORKDIR /app

# Copy installed dependencies from builder stage
COPY --from=builder /app/.venv /app/.venv

# Copy application code
COPY sa sa
COPY models models

# Expose the port
EXPOSE 8000

# Run the application
CMD ["/app/.venv/bin/uvicorn", "sa.app:app", "--host", "0.0.0.0", "--port", "8000"]