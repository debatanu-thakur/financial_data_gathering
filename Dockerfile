# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements-dev.txt requirements-dev.txt
COPY requirements.txt requirements.txt

RUN pip install -r requirements-dev.txt


COPY . /app

CMD [ "python3", "financial/run.py"]