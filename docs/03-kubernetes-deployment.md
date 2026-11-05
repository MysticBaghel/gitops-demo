# Kubernetes Deployment

## Local Cluster

Minikube provides the local Kubernetes environment.

Start the cluster:

```bash
minikube start --driver=docker
```

Verify:

```bash
kubectl get nodes
```

## Namespace

The application runs inside the `gitops-demo` namespace.

```bash
kubectl apply -f k8s/namespace.yaml
```

## Deployment

The Deployment defines the desired number of application replicas and the container image.

```bash
kubectl apply -f k8s/deployment.yaml
```

Verify:

```bash
kubectl get deployments -n gitops-demo
kubectl get pods -n gitops-demo
```

## Service

The application is exposed through a NodePort Service.

```bash
kubectl apply -f k8s/service.yaml
```

Verify:

```bash
kubectl get services -n gitops-demo
```

Access the application:

```bash
minikube service gitops-demo-service -n gitops-demo --url
```

## Self-Healing Demonstration

Kubernetes maintains the desired number of replicas.

Delete a Pod:

```bash
kubectl delete pod <pod-name> -n gitops-demo
```

Kubernetes automatically creates a replacement Pod because the Deployment still requires the configured replica count.

## Kubernetes Dashboard

Enable the Dashboard:

```bash
minikube addons enable dashboard
minikube dashboard
```

The Dashboard provides a visual interface for inspecting workloads, services, namespaces, and cluster resources.