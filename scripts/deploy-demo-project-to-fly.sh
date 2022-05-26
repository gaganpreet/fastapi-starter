#!/bin/bash

cookiecutter --no-input . -f project_slug="demo-project-fastapi-starter" project_name="Demo project FastAPI starter"

cp scripts/fly.toml ./demo-project-fastapi-starter/

cd demo-project-fastapi-starter/

flyctl deploy --remote-only
