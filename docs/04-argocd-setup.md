# Argo CD Setup

## Overview

Argo CD is a declarative GitOps continuous delivery tool for Kubernetes.

It monitors Git repositories and synchronizes Kubernetes resources with the configuration stored in Git.

## Installation

Create the namespace:

```bash
kubectl create namespace argocd
```

Install Argo CD:

```bash
kubectl apply -n argocd --server-side --force-conflicts \
  -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

Verify:

```bash
kubectl get pods -n argocd
```

## Access the Dashboard

Forward the Argo CD server port:

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Open:

```text
https://localhost:8080
```

## Initial Login

Username:

```text
admin
```

Retrieve the initial password:

```bash
kubectl get secret argocd-initial-admin-secret \
  -n argocd \
  -o jsonpath="{.data.password}" | base64 -d
```

## Application Configuration

The Argo CD Application is defined in:

```text
argocd/application.yaml
```

It specifies:

- Git repository URL
- Target branch
- Kubernetes manifest directory
- Destination cluster
- Destination namespace
- Synchronization policy

## Application Status

Argo CD exposes two important status indicators:

- **Synced:** Live resources match the desired Git configuration.
- **Healthy:** Managed resources are considered healthy.