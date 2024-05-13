
# Curson Payment Microservice
This is a microservice that handles payment and order operations for the Curson platform. It is built with FastAPI and uses Docker for containerization. It is not complete because Celery does not support async tasks and therefore I cannot use it for polling stripe checkout sessions and updating Order payment status, and using webhooks would require deployment. The point is, I managed to create this app writing myself next to no lines of code.

## Installation
* Create .env file according to .env.sample
* Run ```docker-compose build```
* Run ```docer-compose up```

## Demo
![screenshot](Screenshot_2024-02-26_12-10-50.png)

