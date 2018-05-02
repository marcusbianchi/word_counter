FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir redis

ENV REDISGRESHOST "redis-container"

ENV MONITOREDFOLDER  "/var/docs/"

COPY . .

ENTRYPOINT ["python", "./app.py"]
