FROM python:3.12-slim

WORKDIR /app

# Install dependencies first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# App Runner will connect to this port
EXPOSE 8000

# Replace main:app if your FastAPI app is elsewhere
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]