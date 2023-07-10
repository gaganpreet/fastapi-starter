# FastAPI-Starter

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/gaganpreet/fastapi-starter/cookiecutter-project-test.yml)

![GitHub last commit (branch)](https://img.shields.io/github/last-commit/gaganpreet/fastapi-starter/main)

A FastAPI based starter that relies heavily on existing plugins/frameworks. Integrates with OpenAPI Generator for a Typescript client, FastAPI Users for authentication, async-first with SQLAlchemy 2.0.

---

## Features

- Uses **best practices**: Factory pattern and environment variables for configuration
- User registration, models, authentication using [**FastAPI Users**](https://github.com/fastapi-users/fastapi-users)
- Modern admin interface using [**React-Admin**](https://marmelab.com/react-admin/)
- **Github Action** for building docker images and running automated tests
- **Dependabot** config to keep project dependencies up to date
- Create Typescript bindings for front-end automatically from OpenAPI spec using [**OpenAPI-Generator**](https://github.com/OpenAPITools/openapi-generator/), no need to write/update code when backend changes
- Async-first codebase with **SQLAlchemy 2.0** and Alembic for database migrations
- **pytest** with example tests included
- Integration tests with **Cypress**
- Docker images for frontend and backend
- Includes extra Dockerfile (backend serves frontend) for straightforward production deployment
- Pre-commit hooks with [Black](https://github.com/psf/black), [autoflake](https://github.com/PyCQA/autoflake), [isort](https://github.com/pycqa/isort), [flake8](https://github.com/PyCQA/flake8), [prettier](https://github.com/prettier/prettier), [eslint](https://github.com/eslint/eslint) for consistent code standards


## How to use

You need Python 3 and pip installed locally. Run the [cookiecutter](https://cookiecutter.readthedocs.io) command (at least 1.7) and you'll be asked a few prompts.

```bash
pip3 install cookiecutter
cookiecutter https://github.com/gaganpreet/fastapi-starter
```

### Input variables

The generator (cookiecutter) will ask you for some data, you might want to have at hand before generating the project.

The input variables, with their default values [default value], are:

* `project_name`: The name of the project
* `project_slug`: The development-friendly name of the project. By default, based on the project name.
* `backend_port`: The backend port on the localhost.
* `front_end_port`: The frontend port on the localhost.


If you want to keep up to date with upstream changes (i.e. changes in this template), then it's better to use [Cruft](https://cruft.github.io/cruft/), which is fully compatible with Cookiecutter.

```bash
pip3 install cruft
cruft create https://github.com/gaganpreet/fastapi-starter
```

Using cruft will generate a metadata file named `.cruft.json` (don't delete it). Later on you can update to the current version of this cookiecutter and import the changes to your generated project by running this command:

```bash
cruft update
```

## Objectives

- Sane defaults with few prompts
- Secure
- KISS principle

## Preview

#### View [live demo](https://demo-project-fastapi-starter.fly.dev) here.

![Login page](assets/login.png)

![Item page](assets/items.png)


## Features not included

The following features were left out in favour of simplicity:

- Celery/Flower/Redis - Not needed for simple projects, Celery can be easily replaced with [background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/).
- Traefik configuration - I prefer [NGINX Proxy automation](https://github.com/evertramos/nginx-proxy-automation)

### Things to do

- [ ] Migrate to Ruff
- [ ] Email templates


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/nadavof"><img src="https://avatars.githubusercontent.com/u/93834717?v=4?s=100" width="100px;" alt="nadavof"/><br /><sub><b>nadavof</b></sub></a><br /><a href="https://github.com/gaganpreet/fastapi-starter/commits?author=nadavof" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://dustindavis.me/"><img src="https://avatars.githubusercontent.com/u/177353?v=4?s=100" width="100px;" alt="Dustin Davis"/><br /><sub><b>Dustin Davis</b></sub></a><br /><a href="https://github.com/gaganpreet/fastapi-starter/commits?author=djedi" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.linkedin.com/in/hugo-tinoco/"><img src="https://avatars.githubusercontent.com/u/43675476?v=4?s=100" width="100px;" alt="Hugo Tinoco"/><br /><sub><b>Hugo Tinoco</b></sub></a><br /><a href="https://github.com/gaganpreet/fastapi-starter/commits?author=h4ndzdatm0ld" title="Documentation">📖</a> <a href="https://github.com/gaganpreet/fastapi-starter/commits?author=h4ndzdatm0ld" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://mixedneeds.com/"><img src="https://avatars.githubusercontent.com/u/158175?v=4?s=100" width="100px;" alt="Michael Bunsen"/><br /><sub><b>Michael Bunsen</b></sub></a><br /><a href="https://github.com/gaganpreet/fastapi-starter/commits?author=mihow" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/alexey-sveshnikov"><img src="https://avatars.githubusercontent.com/u/447089?v=4?s=100" width="100px;" alt="Alexey Sveshnikov"/><br /><sub><b>Alexey Sveshnikov</b></sub></a><br /><a href="https://github.com/gaganpreet/fastapi-starter/commits?author=alexey-sveshnikov" title="Code">💻</a></td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td align="center" size="13px" colspan="7">
        <img src="https://raw.githubusercontent.com/all-contributors/all-contributors-cli/1b8533af435da9854653492b1327a23a4dbd0a10/assets/logo-small.svg">
          <a href="https://all-contributors.js.org/docs/en/bot/usage">Add your contributions</a>
        </img>
      </td>
    </tr>
  </tfoot>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
