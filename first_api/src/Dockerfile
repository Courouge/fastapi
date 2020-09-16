FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8 as base
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY requirements.txt /usr/src/app/requirements.txt
# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/src/app/requirements.txt
COPY . /usr/src/app/
COPY .version /usr/src/app/
