ARG PYTHON_VER=3.10

FROM python:${PYTHON_VER} AS base

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install --no-root

COPY . /app

FROM python:3.10-slim

WORKDIR /app

COPY --from=base /app /app
COPY --from=base /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=base /usr/local/bin /usr/local/bin

CMD uvicorn --host 0.0.0.0 --port 8000 main:app
