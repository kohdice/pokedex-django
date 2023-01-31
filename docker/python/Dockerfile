FROM python:3.10-bullseye

WORKDIR /workspace

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/workspace
ENV POETRY_HOME=/opt/poetry

RUN apt-get update && apt-get install -y vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sSL https://install.python-poetry.org | python - --git https://github.com/python-poetry/poetry.git@master \
    && cd /usr/local/bin \
    && ln -s /opt/poetry/bin/poetry \
    && poetry config virtualenvs.create false

COPY ./pyproject.toml* ./poetry.lock* ./

RUN poetry install
