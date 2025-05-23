FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY docker-entrypoint.sh .

RUN chmod +x docker-entrypoint.sh

ENV SERVICE_TYPE=web
ENV REDIS_URL=redis://localhost:6379
ENV PORT=5000

ENTRYPOINT ["./docker-entrypoint.sh"]
