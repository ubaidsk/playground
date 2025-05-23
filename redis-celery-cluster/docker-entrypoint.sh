#!/bin/bash

if [ "$SERVICE_TYPE" = "web" ]; then
    echo "Starting Flask application..."
    python app.py --redis-url "$REDIS_URL" --port "$PORT"
elif [ "$SERVICE_TYPE" = "worker" ]; then
    echo "Starting Celery worker..."
    celery -A app.celery worker --loglevel=info
else
    echo "Please set SERVICE_TYPE to 'web' or 'worker'"
    exit 1
fi
