# Application and Docker

## FastAPI Application

The project uses a lightweight FastAPI application to demonstrate containerization and Kubernetes deployment.

### Endpoints

| Endpoint | Description |
|---|---|
| `/` | Returns application information and running status |
| `/health` | Returns a simple application health response |
| `/metrics` | Exposes HTTP and application metrics for Prometheus |
| `/docs` | Interactive Swagger API documentation |

The `/metrics` endpoint is exposed by `prometheus-fastapi-instrumentator`. The application is also instrumented with OpenTelemetry so that incoming FastAPI requests can produce distributed traces.

## Dependencies

Application dependencies are listed in `requirements.txt`:

- `fastapi` and `uvicorn[standard]` — API framework and ASGI server.
- `prometheus-fastapi-instrumentator` — exposes Prometheus metrics.
- `opentelemetry-distro[otlp]` — OpenTelemetry distribution and OTLP support.
- `opentelemetry-instrumentation-fastapi` — FastAPI instrumentation.

## Dockerfile

The Dockerfile uses `opentelemetry-instrument` to start Uvicorn with automatic OpenTelemetry instrumentation enabled.

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --timeout=300 --retries=10 -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["opentelemetry-instrument", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

`opentelemetry-instrument` is provided by the installed OpenTelemetry packages. In Kubernetes, the Deployment supplies the service name and OTLP collector endpoint through environment variables. The current Deployment sends traces to Jaeger at `http://jaeger.monitoring.svc.cluster.local:4318` using OTLP over HTTP/protobuf.

## Build the Image Locally

Run these commands from the repository root:

```bash
docker build --network=host -t gitops-demo:v1 .
```

## Run the Container Locally

```bash
docker run --rm -d \
  --name gitops-demo \
  -p 8000:8000 \
  gitops-demo:v1
```

## Verify the Application

```bash
curl http://localhost:8000/
curl http://localhost:8000/health
curl http://localhost:8000/metrics
```

Open the interactive API documentation at `http://localhost:8000/docs`.

Stop the local container when finished:

```bash
docker stop gitops-demo
```

## Publish an Image to Docker Hub (Manual Alternative)

The normal project pipeline builds and pushes images through GitHub Actions. For a manual test, authenticate to Docker Hub and push a tagged image:

```bash
docker login

docker tag gitops-demo:v1 baghelgaurav/gitops-demo:v1
docker push baghelgaurav/gitops-demo:v1
```

The Kubernetes Deployment uses an image from `baghelgaurav/gitops-demo`. In the automated workflow, GitHub Actions tags each image with `sha-<7-character-commit-sha>` and commits that image tag to `k8s/deployment.yaml`; Argo CD then reconciles the cluster to the manifest stored in Git.
