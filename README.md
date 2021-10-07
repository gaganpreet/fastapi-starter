# FastAPI-Starter

A FastAPI based starter that relies heavily on existing plugins/frameworks to create an almost no-code experience. The goal is to build a template that can be used as a starting point for any FastAPI based project.

## How to use

You need Python 3 and pip installed locally. Run the cookiecutter command and you'll be asked a few prompts.

```bash
pip3 install cookiecutter
cookiecutter https://github.com/gaganpreet/fastapi-starter
```

## Objectives

* Sane defaults with few prompts
* Secure
* KISS principle


## Preview

![Login page](assets/login.png)

![Item page](assets/items.png)


## Features

* Uses best practices: Factory pattern and environment variables for configuration
* User registration, models, authentication using [FastAPI Users](https://github.com/fastapi-users/fastapi-users)
* Modern admin interface using [React-Admin](https://marmelab.com/react-admin/)
* Github Action for building docker images and testing and dependabot config to keep project dependencies up to date
* Create Typescript bindings for front-end automatically from OpenAPI spec using [OpenAPI-Generator](https://github.com/OpenAPITools/openapi-generator/), no need to write/update code when backend changes
* [FastAPI CRUD Router](https://github.com/awtkns/fastapi-crudrouter) - [WIP] No need to rewrite generic CRUD routes
* SQLAlchemy 1.4 ORM (in future mode, with 2.0 style API) and Alembic for database migrations
* pytest with example tests included


## Features not included

The following features were left out in favour of simplicity:

* Celery/Flower/Redis - Not needed for simple projects, Celery can be easily replaced with [background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/).
* Traefik configuration - I prefer [NGINX Proxy automation](https://github.com/evertramos/nginx-proxy-automation)


### Things to do

- [x] Fix docker setup
- [x] Create Github action
- [x] Dependabot config
- [x] Add pre-commit hooks: Black, isort, flake8, mypy, tslint
- [x] Setup FastAPI CRUD example
- [ ] Coverage report in tests
- [ ] Email templates
- [ ] Deployment instructions: Possibly provide an option to create a single docker image (where FastAPI serves static assets) that can be easily deployed
- [ ] Async SQLAlchemy
