##  size 95.8MB  ##

FROM python:3-slim AS build-env
ADD app /app
ADD requirements.txt /app
WORKDIR /app
RUN pip3 install --no-cache-dir --disable-pip-version-check -r requirements.txt -t /app

FROM gcr.io/distroless/python3-debian10
COPY --from=build-env /app /app
WORKDIR /app
CMD ["main.py"]