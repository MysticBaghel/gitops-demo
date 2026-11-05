# GitOps Workflow using Argo CD on Kubernetes

A hands-on implementation of GitOps using Argo CD, Kubernetes, Docker, and GitHub.

## Overview

This project demonstrates automated deployment and continuous reconciliation of a containerized FastAPI application on a local Kubernetes cluster.

Argo CD monitors Kubernetes manifests stored in GitHub and synchronizes the cluster with the desired configuration.

## Technology Stack

- **Application:** Python, FastAPI
- **Containerization:** Docker
- **Container Registry:** Docker Hub
- **Orchestration:** Kubernetes, Minikube
- **GitOps:** Argo CD
- **Version Control:** Git, GitHub

## Architecture

```text
Developer
    |
    v
GitHub Repository
    |
    v
Argo CD
    |
    v
Kubernetes Cluster
    |
    v
FastAPI Deployment
    |
    v
FastAPI Pods
```

## Key Features

- Containerized FastAPI application
- Kubernetes Deployment and Service
- Declarative infrastructure configuration
- Automated synchronization from Git
- Self-healing and drift correction
- Resource pruning

## Repository Structure

| Directory | Purpose |
|---|---|
| `k8s/` | Kubernetes manifests |
| `argocd/` | Argo CD Application configuration |
| `docs/` | Technical documentation |

## Documentation

1. [Architecture](docs/01-architecture.md)
2. [Application and Docker](docs/02-application-and-docker.md)
3. [Kubernetes Deployment](docs/03-kubernetes-deployment.md)
4. [Argo CD Setup](docs/04-argocd-setup.md)
5. [GitOps Workflow](docs/05-gitops-workflow.md)
6. [Testing and Validation](docs/06-testing-and-validation.md)
7. [Troubleshooting](docs/07-troubleshooting.md)

## Getting Started

```bash
git clone https://github.com/MysticBaghel/gitops-demo.git
cd gitops-demo
```

See the [documentation](docs/) for setup and deployment instructions.

## Author

**Gaurav Singh Baghel**

[GitHub Profile](https://github.com/MysticBaghel)