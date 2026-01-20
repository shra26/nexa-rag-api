[README.md](https://github.com/user-attachments/files/24726097/README.md)

# Containerize a RAG API with Docker


**Author:** Shravanth Venkatesh  

---

![Image](http://learn.nextwork.org/optimistic_rose_kind_soursop/uploads/ai-devops-docker_x7y8z9a0)

---

## Introducing Today's Project!

In this project, I will demonstrate competence in building docker image. I'm doing this project to brush up in commands and docker standards that have changed over the years.

### Key services and concepts

Services I used were.. Key concepts I learnt include...

### Challenges and wins

This project took me approximately... The most challenging part was... It was most rewarding to..

### Why I did this project

I did this project because..

---

## Setting Up the RAG API

In this step, I'm setting up the code for the RAG API. The RAG API is an interface to add and query the knowledge base and the locally running model.

### API setup and workspace

In this step, I'm creating a virtual environment. A virtual environment is a workspace that allows specific version of package dependencies to exist together without changing unless specified. I need it because i want to package it up into a docker image.

### Dependencies installed

The packages I installed are chromadb, fastapi, ollama, uvicorn. FastAPI is used for creating the server endpoints. Chroma is used for storing the knowldge base in the form of numeric sequences called vector embeddings from converting the input text. Uvicorn is used for serving the endpoints. Ollama is used for hosting and running the model locally..

![Image](http://learn.nextwork.org/optimistic_rose_kind_soursop/uploads/ai-devops-docker_c9d0e1f2)

### Local API working

I tested that my API works by runing a GET call against it. The local API responded with the right data. This confirms that data was ingested by the model from the knowledge base.

![Image](http://learn.nextwork.org/optimistic_rose_kind_soursop/uploads/ai-devops-docker_v5w6x7y8)

---

## Installing Docker Desktop

### Docker Desktop setup

Docker Desktop is a container creator/runner. I installed it because I want to create and run a container. Containerization will help my project by locking in the dependecies and make it usable across any docker application on another sytem.

### Docker verification

I verified Docker is working by installing the hello-world container image from docker. The hello-world container proves that all dependencies for docker as installed and I can proceed in working with docker and access all its functionality.

![Image](http://learn.nextwork.org/optimistic_rose_kind_soursop/uploads/ai-devops-docker_i9j0k1l2)

---

## Creating the Dockerfile

In this step, I'm building a RAG API. RAG stands for Retrival augmented generation. I'm creating files like dockerfile and build the docket image.

### How the Dockerfile works

A Dockerfile is the file used to build your image. The key instructions in my Dockerfile are adding the files/dependencies we want run to the image and create the image. FROM tells Docker to choose the base image. COPY is used for choose the files to be added to the image. RUN executes commands as pre compute commands and are added into the image and is ready to go when the image is loaded onto docker. CMD defines the post image start commands to be run when the image is loaded onto docker.

### Containerized API test results

Testing the API after containerization proved that we can containerize our api and have it connect to a host ollama. The difference between running locally and in Docker is all dependencies are within the image, works the same everywhere, isolated form host system. Containerization helps because it adds structure, standardization and portability to software

![Image](http://learn.nextwork.org/optimistic_rose_kind_soursop/uploads/ai-devops-docker_o1p2q3r4)

---

## Building and Running the Container

### Docker image build complete

Building a Docker image involves making the core files. I verified my Docker image was built successfully by running "docker images | grep name". This confirms that my API is now containerized because there is an image created for it.

![Image](http://learn.nextwork.org/optimistic_rose_kind_soursop/uploads/ai-devops-docker_p9q0r1s2)

![Image](http://learn.nextwork.org/optimistic_rose_kind_soursop/uploads/ai-devops-docker_x7y8z9a0)

---

## Pushing to Docker Hub

In this project extension, I'm pushing to Docker Hub. Docker Hub is a cloud repository of images generater by the docker software. I'm doing this because I want to use the image on cloud providers and ci/cd pipeline integration.

### Docker Hub push complete

I pushed to Docker Hub by connecting to the docker hub with my  login. Docker Hub is useful because it aloows to share built images with the team. The advantage of pushing to a registry is it can be accessed from anywhere in the worls remotly and have it behave the same way constantly, therefore giveing it critical reliability.

![Image](http://learn.nextwork.org/optimistic_rose_kind_soursop/uploads/ai-devops-docker_m5n6o7p8)

### Pulling from Docker Hub

Pulling an image from Docker Hub means i am downloading the image. When I ran docker pull, Docker downloaded the image from the docket hub cloud. The difference between building locally and pulling from Docker Hub is the image build location is different.

![Image](http://learn.nextwork.org/optimistic_rose_kind_soursop/uploads/ai-devops-docker_f5g6h7i8)

---

---
