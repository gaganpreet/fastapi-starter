# FastAPI-Starter

Note: This project is pre-alpha at the moment.

A FastAPI based starter that relies heavily on existing plugins to create an almost no-code experience. The goal is to build a template that can be used as a starting point for any FastAPI based project and go from 0 to 100 within seconds. 🙂 🚀

## Objectives

* Sane defaults with few prompts
* Secure
* KISS principle

## Features

* Uses best practices: Factory pattern and environment variables for configuration
* User registration, models, authentication using [FastAPI Users](https://github.com/fastapi-users/fastapi-users)
* Modern admin interface using [React-Admin](https://marmelab.com/react-admin/)
* Create Typescript bindings for front-end automatically from OpenAPI spec using [OpenAPI-Generator](https://github.com/OpenAPITools/openapi-generator/), no need to write/update code when backend changes
* [FastAPI CRUD Router](https://github.com/awtkns/fastapi-crudrouter) - [WIP] No need to rewrite generic CRUD routes
* SQLAlchemy 1.4 ORM (in future mode, with 2.0 style API) and Alembic for database migrations
* pytest with example tests included


## Features not included

The following features were left out in favour of simplicity:

* Celery/Flower/Redis - Not needed for simple projects, Celery can be easily replaced with background tasks.
* Traefik configuration - I prefer [NGINX Proxy automation](https://github.com/evertramos/nginx-proxy-automation)


### Things to do

- [x] Fix docker setup
- [x] Create Github action
- [x] Dependabot config
- [ ] Coverage report in tests
- [x] Add pre-commit hooks: Black, isort, flake8, mypy, tslint
- [ ] Setup FastAPI CRUD example
- [ ] Email templates
- [ ] Deployment instructions: Possibly provide an option to create a single docker image (where FastAPI serves static assets) that can be easily deployed
- [ ] Async SQLAlchemy
