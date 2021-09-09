#! /usr/bin/env bash

set -eou pipefail

(cd ./test-project && docker-compose down --rmi local -v && cd ..) || true

# Run this from the root of the project
rm -rf ./test-project

cookiecutter --no-input -f ./ project_slug="test-project"

cd ./test-project/

docker-compose up -d

docker-compose exec postgres createdb -U postgres apptest

docker-compose exec backend pytest -v

docker-compose down --rmi local -v