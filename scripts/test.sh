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


apt-get update -qq
# Packages needed by cypress
apt-get install -qq xvfb libnss3 libatk1.0 libatk-bridge2.0 libgtk-3.0 libgbm1 libasound2
# Packkages needed by openapi generator
apt-get install -qq default-jre

###################
# Run e2e tests
cd frontend

yarn run-e2e-tests


###################
# Compare generated openapi client with the one in the repo
mv src/generated src/generated-backup
yarn genapi
diff -r src/generated-backup src/generated || (echo "Generated files changed. Please make sure they are in sync" && exit 1)
