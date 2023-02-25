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

mv ./frontend/src/generated /tmp/src-generated

PACKAGE_LIST="xvfb libnss3 libatk1.0 libatk-bridge2.0 libgtk-3.0 libgbm1 libasound2 default-jre"
# If GITHUB_REPOSITORY is not set, then we can just run it in docker
# We need to have two paths here because Github CI works weirdly with bind mounts that we can use to run the tests locally in Docker
if [ -z "${GITHUB_REPOSITORY-}" ]
then
    docker run \
    -v $(pwd)/frontend/src/generated/:/app/src/generated \
    -v $(pwd)/frontend/cypress:/app/cypress \
    --network="host" \
    frontend-build \
    bash -xc "apt-get update -qq &&
        apt-get install -qq $PACKAGE_LIST &&
        yarn run-e2e-tests &&
        yarn config set script-shell /bin/bash &&
        yarn genapi"
else
    cd frontend
    apt-get update -qq && apt-get install -qq "$PACKAGE_LIST"
    yarn run-e2e-tests
    yarn genapi
fi
#
# This is to ensure that the generated API client is always in sync with FastAPI code
diff -r /tmp/src-generated ./frontend/src/generated || (echo "Generated files changed. Please make sure they are in sync" && exit 1)
