# Automate Testing with GitHub Actions

By Shravanth Venkatesh

\|January 2026

# Introducing Today's Project!

In this project, I will demonstrate the usage of github actions to setup a Continous Integration/ Continous Depoyment pipeline for our RAG API built over the last few days. I'm doing this project to implement github actions as the mode of CI/CD over aws code build/deploy.

## Key services and concepts

Services I used were github actions, git, test ai responses. Key concepts I learnt include the ability to test ai responses by making sure we check th econtxt we use by mocking the response in a deterministic way.

## Challenges and wins

This project took me approximately 3 hours. The most challenging part was thinking through the code to get the semantic analysis correctly as i had to look up documentation and understanding it. It was most rewarding to be able ot test the ai deterministically.

## Why I did this project

I did this project because I wanted to learn ci/cd. One thing I'll apply from this is testing patterns in the future.

# Setting Up Your RAG API

I'm setting up my RAG API by usinf fastAPI. A RAG API retrieves information by adding context using knowledge base. This foundation is needed for CI/CD because we need a codebase to deploy from.

# Creating Semantic Tests

I'm creating semantic tests that verify the meaning of the output and whether that is accurate. Unlike unit tests that check code logic, semantic tests validate instead of checking for exact text matches (which would fail due to LLM non-determinism), it checks for the presence of important concepts that should appear in any correct answer about Kubernetes.

## Non-deterministic output observation

When I ran the query multiple times, I noticed the non deterministric nature of the tinyllama model we are using. This is a problem because the answers change and possibly use the context or the trained data information sometimes. For CI/CD to work reliably, we need a semantic analysis of the answer.

# Adding Mock LLM Mode

I'm adding mock LLM mode to test the llm in a deterministic way. This solves the non-determinism problem by outputting the retrieved data instead of generated data. Reliable testing requires deterministic answers.

## Mock LLM mode for CI testing

Mock LLM mode returns the retrieved text directly, which makes tests easier. Without mock mode, tests would non deterministic. For automated CI, we need to be deterministic.

# Creating GitHub Actions Workflow

I'm creating a GitHub Actions workflow file that will automate testing. The workflow automates testing by using the YAML file. When I push code, it will execute the tests on github servers.

## Workflow automation and CI testing

I created the workflow file in .github/workflows. I pushed it using git add, git commit and git push.. Once on GitHub, the workflow will execute on changes to the k8s.txt, app.py and embed.py pushed into them.

# Testing Data Quality

I'm triggering the CI workflow by making changes to the k8s.txt. The workflow will test execute automatically. I expect it to fail because orchestration was removed.

## Data quality and CI protection

The missing keyword was "orchestration". The semantic test failed because there was no orchestration. Without CI, this degraded content would have broken the prodtion when users would complain about it.

# Scaling with Multiple Documents

I'm restructuring the project to handle real world scenarios where hundreds or thousands of documents will need to be stored. The new folder structure supports this process. This approach scales better because the RAG system can handle multiple knowledge documents.

## Docs folder structure and CI scaling

The docs folder organizes files by moving all docs under docs/ folder. The embed\_docs.py script handles multiple .txt files under docs/ folder. CI validated all documents and found all the required test . This structure supports growth by allowing new docs to be added overtime.
