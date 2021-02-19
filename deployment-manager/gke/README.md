# GKE Cluster, Type and Workloads

This guide is provides a Google Cloud Deployment Manager template which deploys a GKE cluster and a Deployment Manager type. It is based on the guidelines that provided in the following GitHub repository with some adaptations needed due to updated in GKE type providers and Kubernetes API deprecations.

https://github.com/GoogleCloudPlatform/deploymentmanager-samples

In any step of this guide you can also advice the Cloud Deployment Manager documentation, which provides more details on how to create and manage cloud resources with templates.

https://cloud.google.com/deployment-manager

Using Deployment Manager to deploy Kubernetes resources into a new GKE cluster is a two step process, as described below.

1. Create the GKE Cluster resources and Types

```
NAME=appt-cluster-resources
gcloud deployment-manager deployments create ${NAME} --config=cluster-resources.yaml
```

2. Deploy the Service and Workloads

```
NAME=app-cluster-deployment
gcloud deployment-manager deployments create ${NAME} --config=app-resources.yaml
```

## Additional Resources

### Kubernetes API

[Kubernetes Deployment API](https://kubernetes.io/docs/reference/kubernetes-api/workloads-resources/deployment-v1/#create-create-a-deployment)

[Kubernetes Service API](https://kubernetes.io/docs/reference/kubernetes-api/services-resources/service-v1/#create-create-a-service)
