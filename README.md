# Deploy a RAG API to Kubernetes

By Shravanth Venkatesh

\|January 2026

<img width="1018" height="395" alt="Screenshot 2026-01-20 at 10 09 21 PM" src="https://github.com/user-attachments/assets/4bb14b72-11eb-4015-8695-b21299a517a4" />


<img width="1128" height="424" alt="image" src="https://github.com/user-attachments/assets/e0b89689-f3d5-4786-ac16-c5f57b751a5f" />


# Introducing Today's Project!

In this project, I will deploy the RAG API built in the previous exercise to Kubernetes. I'm doing this project to learn quick Kubernetes depoyment. Kubernetes will help me deploy and manage continers in a real production environment.

## Key services and concepts

Key concepts I learnt include kubectl and minikube. Kubernetes provides deployment management service. Deployments manage the replica sets. Services route the endpoint call to the right pod based on tags/ namespaces.

## Challenges and wins

This project took me approximately 4 hours. The most challenging part was getting comms up between pods and ollama the model provider to work. It was most rewarding to truly understand the capabilities of kubernetes.

## Why I did this project

I did this project because I wanted to learn Kubernetes. One thing I'll apply from this is how to leverage control plane to manage the pods in a large scale.

# Setting Up My Docker Image

In this step, I'm setting up docker. I need a Docker image because Kubernetes decides where the images run, how many to run and keeps the continers alive but it never builds the image itself.

<img width="1368" height="120" alt="image" src="https://github.com/user-attachments/assets/27373e09-603b-4d56-8813-c65819201c63" />


## What the Docker image contains

I ran docker images and saw the docker image creaeted. The image size was nexa-rag-app-2:latest. The IMAGE ID was ff77a67a5876.

# Installing Kubernetes Tools

In this step, I'm installing minikube and kubectl. I need these tools because the former runs the k8s cluster and the latter is used to control it.

<img width="1368" height="98" alt="image" src="https://github.com/user-attachments/assets/2c212441-589a-49af-9fe1-f44f3e69ab17" />


## Verifying the tools are installed

I installed Minikube using brew. I installed kubectl by running brew install kubectl. I could tell both installations were successful by running "minikube version" and "kubectl version --client"

# Starting My Kubernetes Cluster

In this step, I'm starting a minikube cluster. Minikube will create the cluster. I also need to load my image onto it for the node to come up.

<img width="1044" height="96" alt="image" src="https://github.com/user-attachments/assets/4d20ccad-7771-44e8-9dca-f3e40487458e" />


## Loading the Docker image into Minikube

I started the cluster by running "minikube start". and saw the minikube control-plane installed using "kubectl get nodes" which also showed the status as ready.

## Why load image into Minikube

The eval minikube docker-env command sets the terminal's env variables referenced by docker to be set to address the minikube container instead of the host system. Without loading the image into Minikube, Kubernetes would need to get the image from AWS EMR or docker image from docker hub.

# Deploying to Kubernetes

In this step, I'm deploying my rag api to k8s. I need a Deployment because i want to give control to k8s to run the app and handles scenarios like
Specifies which container image to run
Defines how many replicas (copies) to run
Handles rolling updates (updating without downtime)
Restarts containers if they crash
Scales your application up or down

<img width="1044" height="860" alt="image" src="https://github.com/user-attachments/assets/099ee680-e5be-4370-95ee-03a49944381d" />


## How the Deployment keeps my app running

The deployment.yaml file tells Kubernetes the desired state if the deployment into the cluster. The key parts are the depoyment name, replicas which denote the number of desired pods, the container image nexa-rag-app-2:latest which we built into the minikube cluster in the previous step and OLLAMA\_HOST which tells the ollama client address in the env variable.

<img width="1178" height="190" alt="image" src="https://github.com/user-attachments/assets/8916d11d-a06d-43c0-98fb-1b0159f82751" />


## What did you observe when checking your pods?

I ran kubectl get pods and saw my running pod. The pod had the name nexa-rag-app-deployment-66b6f87999-4xmtg. and statu RUNNING. which means the pod is good and working fine. The READY column showed how many replicas are running vs how many are desired in this case 1/1. which indicates there is one 1 pod online and active for 1 desired active, which is perfect for this case.

# Creating a Service

In this step, I'm creating a k8s service. I need a Service because i need to consistently connect to the api pod which can change it's IP multiple times as they are ephimeral byt using the service the constant IP with DNS names allocated to the pod running the app.

## What does the service.yaml file do?

The service.yaml file tells Kubernetes how to provide a stable network endpoint for the RAG API Pods.. The selector finds Pods by matching the meta data tags of the pods. The port configuration allows communication of host system with the pods. NodePort enables access from outside by opening up ports on each node of the cluster, allowing accesss from the outside, in this case the host.

<img width="1278" height="122" alt="image" src="https://github.com/user-attachments/assets/5b0ea931-5c41-4005-add3-8db481fc76ba" />


## What kubectl commands did you run to create the service?

I applied my Service file by running "kubectl apply -f service.yml". I then verified that the Service was created by running "kubectl get services".

# Accessing My API Through Kubernetes

In this step, I'm testing that my k8s api is accessible from the host system, mimicking a client connection.

<img width="1128" height="424" alt="image" src="https://github.com/user-attachments/assets/120c1beb-40d0-4d5e-8875-2933061e47fc" />


## How I accessed my API

I tested my API by running the fastapi's swagger ui. The response showed data from the knowledge base stored on it. This confirms that the RAG API is working accurately. The main difference between Docker and Kubernetes deployment is that docker is the container and k8s is the container manager which is open source..

## Request flow through Kubernetes

The request flow went from my computer terminal then to nodeport then to k8s service to pod. The Service routed traffic by sending request to 8000 port on the pods by matching with the metadata tag nexa-rag-api. NodePort enabled access by opening/exposing the port 31859.

# Testing Self-Healing

In this project extension, I'm demonstrating the insane ability to self heal. Self-healing is important because it adds huge capabilites for the softwares we run on the containers to have very little to no downtime. this is a super power which is needed to gaurantee high SLAs for clients in production environments.

<img width="1290" height="442" alt="image" src="https://github.com/user-attachments/assets/3825e42d-6427-4bec-8ed9-4fd6bdcd9fc1" />


## What did you observe when you deleted the pod?

When I deleted the pod, I saw the status change from Terminating, to Pending to ContainerCreating to Running the new pod in less than 1-2 seconds. A new pod was created because the older pod was deleted here, mimicking an actual production service crash or service crash. This is truly a super power compared to standard Auto Scaling Groups which could take upwards of 5-8 mins to bring up a new s AWS EC2 and at lasrge scale orchestration of 1000s of compute pods we can s ee clearly the benefit of using Kubernetes.

<img width="1290" height="1048" alt="image" src="https://github.com/user-attachments/assets/2904d59d-3e86-4b2c-8348-b4acc14d5542" />

## How the Service routed traffic to the new pod

The Service automatically knows about the new pod because it runs a selector on the api tag in the pod metadata and the list in autoupdated in kubernetes. Without Kubernetes this would have led to service disruption. Self-healing is critical in production because it sustains and builds trust in a business by adhering to strict uptime SLAs.
