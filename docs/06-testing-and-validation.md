# Testing and Validation

## Kubernetes Validation

Check the cluster:

```bash
kubectl get nodes
```

Check application resources:

```bash
kubectl get all -n gitops-demo
```

Check Argo CD:

```bash
kubectl get pods -n argocd
```

## Deployment Scaling

Change the replica count in Git:

```yaml
replicas: 2
```

Commit and push the change.

Verify the number of replicas:

```bash
kubectl get deployment gitops-demo -n gitops-demo
```

Expected:

```text
READY   UP-TO-DATE   AVAILABLE
2/2     2            2
```

## Self-Healing Test

Manually scale the live Deployment:

```bash
kubectl scale deployment gitops-demo \
  --replicas=4 \
  -n gitops-demo
```

Argo CD should detect drift and reconcile the live state back to the replica count defined in Git.

## Pruning Test

Remove a managed resource manifest from Git and push the change.

With pruning enabled, Argo CD can remove the corresponding Kubernetes resource.

## Application Health

Check:

- Deployment availability.
- Pod readiness.
- Service configuration.
- Argo CD synchronization status.
- Argo CD application health.

## Evidence

Add screenshots of:

- Kubernetes Dashboard.
- Running FastAPI Pods.
- Argo CD application overview.
- Successful Git-driven scaling.
- Self-healing demonstration.
- Pruning demonstration.

Only mark demonstrations as completed after verifying their results.