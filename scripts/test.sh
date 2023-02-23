#! /usr/bin/env bash

set -eou pipefail

# Stop containers from previous run, if any
(cd ./test-project && docker-compose -f docker-compose.yml down --rmi local -v && cd ..) || true

# Run this from the root of the project
rm -rf ./test-project

cookiecutter --no-input -f ./ project_slug="test-project" project_name="Test project"

cd ./test-project/

# Start docker containers
docker-compose -f docker-compose.yml up -d --build


# Run backend tests
docker-compose exec -T postgres createdb -U postgres apptest

docker-compose exec -T backend pytest -v


# Run cypress tests
docker-compose exec -T backend alembic upgrade head

docker build --target build -t frontend-build:latest frontend

docker run --network host -v $(pwd)/frontend/cypress:/app/cypress frontend-build bash -c "apt-get update && apt-get install -qq xvfb libnss3 libatk1.0 libatk-bridge2.0 libgtk-3.0 libgbm1 libasound2 && yarn run-e2e-tests"

# Bind mount src/generated directory and fail if it changed
# This is to ensure that the generated files are always in sync with FastAPI code
cp -ruv ./frontend/src/generated /tmp/src-generated

docker run --network host frontend-build -v $(pwd)/frontend/src/generated:/app/src/generated bash -c "apt-get update && apt-get install -qq default-jre && yarn config set script-shell /bin/bash && yarn genapi"

diff -r /tmp/src-generated ./frontend/src/generated || (echo "Generated files changed. Please make sure they are in sync" && exit 1)
