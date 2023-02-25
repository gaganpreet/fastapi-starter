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

# If GITHUB_REPOSITORY is not set, then use pwd
if [ -z "${GITHUB_REPOSITORY-}" ]
then
    WORKSPACE=$(pwd)
else
    # https://stackoverflow.com/questions/69609618/github-action-i-wrote-doesnt-have-access-to-repos-files-that-is-calling-the-ac
    PROJECT_NAME="$(basename ${GITHUB_REPOSITORY})"
    WORKSPACE="${RUNNER_WORKSPACE}/${PROJECT_NAME}"
fi

docker run -v $WORKSPACE/frontend/cypress:/app/cypress -i --network host frontend-build bash -c "apt-get update && apt-get install -qq xvfb libnss3 libatk1.0 libatk-bridge2.0 libgtk-3.0 libgbm1 libasound2 && yarn run-e2e-tests"

# This is to ensure that th generated files are always in sync with FastAPI code
mv ./frontend/src/generated /tmp/src-generated

docker run -v $WORKSPACE/frontend/src/generated/:/app/src/generated -i --network host frontend-build bash -c "apt-get update && apt-get install -qq default-jre && yarn config set script-shell /bin/bash && yarn genapi"

diff -r /tmp/src-generated ./frontend/src/generated || (echo "Generated files changed. Please make sure they are in sync" && exit 1)
