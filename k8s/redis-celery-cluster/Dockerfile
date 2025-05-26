FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY docker-entrypoint.sh .

RUN chmod +x docker-entrypoint.sh

ENV SERVICE_TYPE=web
# REDIS_URL must be provided when running the container

ENTRYPOINT ["./docker-entrypoint.sh"]
