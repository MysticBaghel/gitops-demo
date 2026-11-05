from fastapi import FastAPI

app = FastAPI(
    title="GitOps Demo API",
    description="A beginner project for learning Docker and Kubernetes",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Hello from GitOps Demo!",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
