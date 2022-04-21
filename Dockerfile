FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /flask_app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install