# PythonCloudDevOps Repository
### This repository contains a set of Python functions designed to perform different tasks, packaged in Docker for easy deployment and execution. The repository includes the following functionalities:

1. **Cost Calculation:** Given a dictionary of items and their costs, and an array specifying the items bought, it calculates the total cost of the items plus a given tax.

2. **Word Processing:** A function to get the N-th letter from each word in a list of words and form a new Word with them.

3. **Dictionary:** A function that allows you to add a list of words to a dictionary and look for them.

## Requirements
Python 3.x
Docker (for containerized execution)

## Run locally

 To run the Function run the next command inside each folder:

```bash
python main.py
```
### To test run the next command inside the tests folder:

```bash
pytest
```

# Docker Setup
The application is containerized using Docker, allowing you to easily run it in any environment that supports Docker.


## How to Build the Docker Image
Make sure you have Docker installed. If not, install Docker.

In the root directory of this repository (where the Dockerfile is located), run the following command to build the Docker image:

```bash

docker build -t pythonclouddevops .
```
This will create a Docker image tagged as pythonclouddevops.

## How to Run the Docker Container
You can run the Docker container with different functions based on the task you want to execute. The main script (main.py) will handle routing to the appropriate function.
#### Pass Arguments When Running the Container

### 1. Cost Calculation Function
To run the Cost Calculation function, use the following command:

```bash
docker run --rm pythonclouddevops Costs
```
> [!NOTE]
> --rm  is used to automatically remove the container once it stops running. 

### 2. Words function needs to run interactively, run:

```bash
 docker run -it pythonclouddevops Words 1 2 3
 ```
> [!NOTE]
> Give the numbers of your choosing 

### 3. Dictionary function run:

```bash 
docker run pythonclouddevops Dictionary
```