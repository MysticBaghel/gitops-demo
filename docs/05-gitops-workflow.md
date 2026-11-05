# GitOps Workflow

## Overview

GitOps uses Git as the source of truth for application infrastructure configuration.

Argo CD monitors the repository and reconciles the Kubernetes cluster with the desired state.

## Repository Configuration

| Parameter | Value |
|---|---|
| Repository | `https://github.com/MysticBaghel/gitops-demo.git` |
| Branch | `master` |
| Manifest Path | `k8s/` |
| Destination Namespace | `gitops-demo` |

## Automated Synchronization

The Argo CD Application uses automated synchronization.

```yaml
syncPolicy:
  automated:
    enabled: true
    prune: true
    selfHeal: true
```

### Automated Sync

Changes pushed to GitHub are detected by Argo CD and applied to Kubernetes after repository refresh.

### Self-Healing

Argo CD detects differences between Git and live Kubernetes resources and restores the desired configuration.

### Pruning

Resources removed from Git can be deleted from Kubernetes when pruning is enabled.

## Example Workflow

1. Modify a Kubernetes manifest.
2. Commit the change.
3. Push it to GitHub.
4. Argo CD detects the new revision.
5. Argo CD synchronizes Kubernetes.
6. Kubernetes reconciles the requested application state.

## Example: Scaling

Change the Deployment replica count:

```yaml
spec:
  replicas: 2
```

Commit and push:

```bash
git add k8s/deployment.yaml
git commit -m "feat: scale FastAPI deployment"
git push
```

Verify:

```bash
kubectl get pods -n gitops-demo
```