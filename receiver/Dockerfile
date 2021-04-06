FROM python:3.9.0-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /receiver && apt-get update
WORKDIR /receiver

COPY ./pyproject.toml /receiver/
COPY ./poetry.lock /receiver/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY ./ /receiver
