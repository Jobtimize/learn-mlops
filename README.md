# MLOps

A simple MLOps project using sklearn, FastAPI and Pydantic.

## Goal

In a single afternoon, create a minimal MLOps application that is able to:
- Retrieve some toy data (California Housing)
- Train and store a simple ML model
- Serve the model using FastAPI
- Make predictions using an endpoint
- Apply validation to the input data
- Log the steps
- Deploy using Docker

## Get started

- Make sure you have nothing running on 0.0.0.0:8000
- From within this directory, do the following:
    - Build the docker image: `docker build . --tag mlops:0.0.1`
    - Run the docker image with the correct ports: `docker run -d -p 8000:8000 mlops:0.0.1`
    - [Optionally] To watch the logs within the Docker container, copy the ID that is printed in the terminal after the previous command. Then: `watch docker <PASTE ID HERE>`
    - On your local machine, from this directory, run the sample test instance: `sh scripts/make_request.sh`

## Next steps:

- Add a docker-compose.yaml file
- Implement unittests
- Setup CI/CD using GitHub Actions
- Add MLFlow
