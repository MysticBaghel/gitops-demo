# Application and Docker

## FastAPI Application

The project uses a lightweight FastAPI application to demonstrate containerization and Kubernetes deployment.

### Endpoints

| Endpoint | Description |
|---|---|
| `/` | Returns application information |
| `/health` | Returns application health |
| `/docs` | Interactive Swagger documentation |

## Dependencies

Dependencies are defined in `requirements.txt`.

## Dockerfile

The Dockerfile packages the application into a container image.

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --timeout=300 --retries=10 -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Build the Image

```bash
docker build --network=host -t gitops-demo:v1 .
```

## Run the Container

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
```

## Publish to Docker Hub

```bash
docker login

docker tag gitops-demo:v1 baghelgaurav/gitops-demo:v1

docker push baghelgaurav/gitops-demo:v1
```

The published image is consumed by the Kubernetes Deployment.