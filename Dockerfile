FROM python:3.11-slim-buster

WORKDIR /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc libpq-dev \
  && apt-get clean


COPY ./requirements.txt /app
RUN pip install -r requirements.txt

ENV PYTHONPATH=/app
