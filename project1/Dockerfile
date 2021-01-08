FROM python:3.8-slim-buster

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY app /app

WORKDIR /app

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]