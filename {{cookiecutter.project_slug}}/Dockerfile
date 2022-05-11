# This monolith Dockerfile:
# Uses FastAPI to serve static assets
# Uses gunicorn as a process manager to run the FastAPI app

FROM node:16 as frontend-build

WORKDIR /app

COPY frontend/package.json frontend/yarn.lock /app/

RUN yarn

COPY frontend /app/

RUN yarn build


FROM python:3.8

WORKDIR /app

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY backend/pyproject.toml backend/poetry.lock /app/

RUN poetry install --no-root

COPY backend /app

COPY --from=frontend-build /app/build /app/static

CMD gunicorn -k uvicorn.workers.UvicornWorker -b :{{ cookiecutter.backend_port }} main:app
