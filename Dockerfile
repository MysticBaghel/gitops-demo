# 1. Choose Python as our base environment
FROM python:3.12-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy dependency file
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir --timeout=300 --retries=10 -r requirements.txt

# 5. Copy application code
COPY . .

# 6. Document application port
EXPOSE 8000

# 7. Start FastAPI application
CMD ["opentelemetry-instrument", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
