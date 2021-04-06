FROM python:3.9.0-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /sender && apt-get update
WORKDIR /sender

COPY ./pyproject.toml /sender/
COPY ./poetry.lock /sender/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY ./ /sender
