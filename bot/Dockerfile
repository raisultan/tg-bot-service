FROM python:3.9.0-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /bot && apt-get update && apt-get install -y gettext
WORKDIR /bot

COPY ./pyproject.toml /bot/
COPY ./poetry.lock /bot/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY ./ /bot
