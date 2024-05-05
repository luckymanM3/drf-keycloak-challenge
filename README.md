# Coding Challenge

# Setup
This project cotains a fresh setup of Django Rest Framework, a PostgreSQL Database and an Keycloak instance for authentication. All of them are orchestrated as Docker Images within a Docker Compose instance.

## What is needed to start it up
1. Docker >4.22.0
2. Python >3.9

## Project Start
1. Run `docker-compose -f docker-compose.yml build` on the root of the project folder
2. Run `docker-compose -f docker-compose.yml up` next
3. The backend will be available on localhost:8000 and Keycloak on localhost:8080

# Task
1. Create and endpoint via django rest framework that is available under `localhost:8000/api/clients`
    1. This endpoint should have have the following Methods available: `GET` `POST` `DELETE`
    2. The model behind it should be build like this `{
        id: {UUID},
        name: {First name},
        address: {Fictional Address of client}
    }`
2. Replace the default django user authentication with a keycloak authentication
    1. Create a new realm called "management" in keycloak via the web interface
    2. Create a test user with credentials by you choice within this realm
    3. Use mozilla_django_oidc for example to create the authentication endpoints in django rest framework
    4. Test the endpoints and authenticate the user you created before
    5. Secure the newly created endpoint `/clients` with a newly created authentication class that uses keycloak instead of django

# Goal
New clients should be able to be created via the endpoint `/clients` and this should be only possible with a authenticated keycloak user. This can be tested via Postman.