![example workflow](https://github.com/capmichal/python_aws/actions/workflows/docker-image.yml/badge.svg)
# Python / Github Actions Pipeline

## Pipeline
The main goal of this project was to ensure continuous integration and deployment of docerized applications to AWS ECS Fargate service.

Workflow:
- Developer updates source code
- Code builds into docker image
- Image gets pushed into AWS ECR
- AWS ECS automatically runs task defined in taskdef.json on given cluster
- Webapp is available via port 5000 on our serverless service 

I chose Fargate instead of managed EC2 instance just for the simplicity 

## Application
A small Python web application written using Flask. Application gets basic information about current and former NBA players based on user's input. Code is short and simple, developing this app was not a goal of this project - I only cared about automation.

Application makes use of an amazing API from: https://app.balldontlie.io/

## Pipeline Visualization
<img width="763" alt="image" src="https://github.com/capmichal/python_aws/assets/130446782/ae369637-4725-4e65-9638-9efc663f029d">
