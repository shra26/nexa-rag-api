
# Build a RAG API with FastAPI

**Author:** Shravanth Venkatesh 

---

![Image](http://learn.nextwork.org/optimistic_rose_kind_soursop/uploads/ai-devops-api_g3h4i5j6)

---

## Introducing Today's Project!

In this project, I will demonstrate ability to create a rag api. I'm doing this project to learn local model running 

### Key services and concepts

Services I used were ollama, fastapi, uvicorn, chromdb. Key concepts I learnt include building a local model and adding context from chromadb as a RAG API.

### Challenges and wins

This project took me approximately 2 hours . The most challenging part was connecting github...a diversion that was not needed. It was most rewarding to creating the the api.

### Why I did this project

I did this project because i wanted to create the rag api

---

## Setting Up Python and Ollama

In this step, I'm setting up Python and Ollama. Python is scripting language.  Ollama is a tool use to run the models on local system. I need these tools because I want to create a RAG system and run models locally on my system.

### Python and Ollama setup

![Image](http://learn.nextwork.org/optimistic_rose_kind_soursop/uploads/ai-devops-api_i9j0k1l2)

### Verifying Python is working

### Ollama and tinyllama ready

Ollama is a tool that will help me run models locally on my system. I downloaded the tinyllama model because it is a light weight model that I will use to run out RAG system and be the brains of the operation. The model will help my RAG API by processing the requests for infromation in a meaningful way.

---

## Setting Up a Python Workspace

In this step, I'm setting up upa project folder. I need it because i want to create a workspace and install the dependecies for the virtual env that is created in the folder level, this is done so that there is no clash in the dependecies on the project with other projects  i might have in other folders and use python.

### Python workspace setup

### Virtual environment

A virtual environment is local env for the folder and has custom env variables . I created one for this project to edit local dependencies. Once I activate it will use the local env variables rather than system env variables. To create a virtual environment, I used the source venv/bin/activate command.

### Dependencies

The packages I installed are fastapi, uvicorn, ollama and chromadb. FastAPI is used for building the api... Chroma is used for retrieval of vector embeddings... Uvicorn is used for server of the fastapi code... Ollama is used for programmatically connecting to the ollama model tinyllama.

![Image](http://learn.nextwork.org/optimistic_rose_kind_soursop/uploads/ai-devops-api_u1v2w3x4)

---

## Setting Up a Knowledge Base

In this step, I'm creating a knowledge base... A knowledge base is a collection of docs to give the model newer data. I need it because to provide fresher data to the model to geneeratte the answer.

### Knowledge base setup

![Image](http://learn.nextwork.org/optimistic_rose_kind_soursop/uploads/ai-devops-api_t1u2v3w4)

### Embeddings created

Embeddings are binary representation of token. I created them by adding data to the chromadb which ran the embedding script to generate the embeddings. The db/ folder contains the embeddings uploaded. This is important for RAG because it matches symantically based on meaning rather than key matching, same meaning embeddings are grouped closer in the chromadb

---

## Building the RAG API

In this step, I'm building a RAG API. An API is Application Protocol Interface. FastAPI is ia a quick api creator package within python. I'm creating this because i want to connect the RAG system that I create here to the internet or another person to use it by calling on this API.

### FastAPI setup

### How the RAG API works

My RAG API works by pulling in the data that is related by using chromadb search and adding it to context of the query sent to the model, this enhances the augmentation of the data sent to the model which does the generation.

![Image](http://learn.nextwork.org/optimistic_rose_kind_soursop/uploads/ai-devops-api_f3g4h5i6)

---

## Testing the RAG API

In this step, I'm testing my RAG API. I'll test it using... Swagger UI is... I'll use it to...

### Testing the API

### API query breakdown

I queried my API by curling into the api created. The command I used was... This command works by... The API responded with...

![Image](http://learn.nextwork.org/optimistic_rose_kind_soursop/uploads/ai-devops-api_g3h4i5j6)

### Swagger UI exploration

Swagger UI is the fastapi interactive UI for the api. I used it to test the /query endpoint. by... The best part about using Swagger UI was the UI and no need to create the curl command by hand.

---

## Adding Dynamic Content

In this project extension, I'm making a dynamic way to populate the chromadb contextual data.

### Adding the /add endpoint

![Image](http://learn.nextwork.org/optimistic_rose_kind_soursop/uploads/ai-devops-api_w9x0y1z2)

### Dynamic content endpoint working

The /add endpoint allows me to add knowledge to the knowledge base in my local setup. This is useful because be adds knowledge to the model and provides context.

---

---
