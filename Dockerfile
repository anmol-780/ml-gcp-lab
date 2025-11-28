FROM python:3.9-slim

WORKDIR /app

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY api/ ./api/
COPY models/ ./models/

# Cloud Run requires port 8080
EXPOSE 8080

CMD ["python", "api/main.py"]
