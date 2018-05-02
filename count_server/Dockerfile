FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir flask redis

ENV REDISGRESHOST "redis-container"

COPY . .

ENTRYPOINT ["python", "./app.py"]

EXPOSE 5000