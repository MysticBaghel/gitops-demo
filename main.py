
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title="GitOps Demo API",
    description="A beginner project for learning Docker and Kubernetes with observability",
    version="1.1.0"
)

# Expose HTTP metrics for Prometheus
Instrumentator().instrument(app).expose(
    app,
    endpoint="/metrics",
    include_in_schema=False
)


@app.get("/")
def home():
    return {
        "message": "Hello from GitOps Demo!",
        "version": "1.1.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
