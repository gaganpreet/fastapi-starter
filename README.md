## FastAPI-Starter

Note: This project is pre-alpha at the moment.

A FastAPI based starter that relies heavily on existing plugins to create an almost no-code experience. The goal is to build a template that can be used as a starting point for any FastAPI based project and go from 0 to 100 within seconds. 🙂 🚀

### Objectives

* Sane defaults without too much configuration
* Secure
* KISS principle

### Packages used

* [FastAPI Users](https://github.com/fastapi-users/fastapi-users) - Provides user registration, models, authentication etc.
* [React-Admin](https://marmelab.com/react-admin/) - Almost zero-effort admin interface using discovered interfaces
* [FastAPI CRUD Router](https://github.com/awtkns/fastapi-crudrouter) - [WIP] No need to rewrite generic CRUD routes


And for cases where react-admin is not enough:

* [OpenAPI-Generator](https://github.com/OpenAPITools/openapi-generator/) - Creates Typescript API directly using FastAPI OpenAPI spec, no need to write implementations to interact with backend.

### Things to do

- [ ] Fix docker setup
- [ ] Create Github action
- [ ] Dependabot config
- [ ] Coverage report in tests
- [ ] Add pre-commit hooks: Black, isort, flake8, mypy, tslint
- [ ] Setup FastAPI CRUD example
- [ ] Email templates
- [ ] Deployment instructions: Possibly provide an option to create a single docker image (where FastAPI serves static assets) that can be easily deployed
