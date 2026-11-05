# Troubleshooting

## Docker Permission Denied

Error:

```text
permission denied while trying to connect to the Docker API
```

Add the current user to the Docker group:

```bash
sudo usermod -aG docker $USER
```

Log out of the desktop session and log back in.

Verify:

```bash
id
docker ps
```

Docker group membership grants root-equivalent privileges.

## Minikube Startup

Start Minikube:

```bash
minikube start --driver=docker
```

Verify:

```bash
kubectl get nodes
```

## Pod Status Issues

Inspect Pods:

```bash
kubectl get pods -A
```

Inspect a specific Pod:

```bash
kubectl describe pod <pod-name> -n <namespace>
```

Inspect logs:

```bash
kubectl logs <pod-name> -n <namespace>
```

## Argo CD Pod Status

Inspect Argo CD components:

```bash
kubectl get pods -n argocd
```

Inspect events:

```bash
kubectl get events -n argocd --sort-by=.lastTimestamp
```

## Argo CD Dashboard Access

Start port forwarding:

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Open:

```text
https://localhost:8080
```

The local installation uses a self-signed TLS certificate, which can trigger a browser warning.

## GitHub Push Failure

Verify the remote:

```bash
git remote -v
```

Verify branch tracking:

```bash
git branch -vv
```

Push:

```bash
git push
```

For an initial push:

```bash
git push -u origin master
```

## Argo CD Not Detecting Changes

Check the latest commit:

```bash
git log -1 --oneline
```

Verify the remote branch:

```bash
git ls-remote origin refs/heads/master
```

Refresh the application in Argo CD and inspect its synchronization status.

## Application Inspection

```bash
kubectl get all -n gitops-demo
kubectl describe deployment gitops-demo -n gitops-demo
```