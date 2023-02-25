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

echo "GITHUB_WORKSPACE_BEFORE", ${GITHUB_WORKSPACE}
# Use GITHUB_WORKSPACE if set, otherwise use current directory
# This is needed for running the tests in GitHub Actions
if [ -z "${GITHUB_WORKSPACE:-}" ]; then
    GITHUB_WORKSPACE=$(pwd)
fi

echo "GITHUB_WORKSPACE_AFTER", ${GITHUB_WORKSPACE}
find ${GITHUB_WORKSPACE}/frontend/
find ${GITHUB_WORKSPACE}/frontend/cypress | grep -v node_modules

docker run --network host frontend-build -v ${GITHUB_WORKSPACE}/frontend/cypress/:/app/cypress bash -c "apt-get update && apt-get install -qq xvfb libnss3 libatk1.0 libatk-bridge2.0 libgtk-3.0 libgbm1 libasound2 && find /app/ && yarn run-e2e-tests"

# Bind mount src/generated directory and fail if it changed
# This is to ensure that the generated files are always in sync with FastAPI code
mv ./frontend/src/generated /tmp/src-generated

docker run --network host frontend-build -v ${GITHUB_WORKSPACE}/frontend/src/generated/:/app/src/generated bash -c "apt-get update && apt-get install -qq default-jre && yarn config set script-shell /bin/bash && yarn genapi"

diff -r /tmp/src-generated ./frontend/src/generated || (echo "Generated files changed. Please make sure they are in sync" && exit 1)
