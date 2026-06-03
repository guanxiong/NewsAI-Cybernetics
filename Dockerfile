FROM python:3.12-slim

WORKDIR /app

# Copy scripts
COPY scripts/ ./scripts/

# Create Inbox directory
RUN mkdir -p Inbox

# Default: run acquire once
ENTRYPOINT ["python3", "scripts/acquire.py"]
CMD ["--source", "all", "--limit", "20", "--classify"]
