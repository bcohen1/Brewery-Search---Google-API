# syntax=docker/dockerfile:1.2

FROM python:3.9-slim-buster

WORKDIR /Docker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY breweries.py .