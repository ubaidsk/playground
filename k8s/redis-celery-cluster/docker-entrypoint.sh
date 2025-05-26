#!/bin/bash

if [ -z "$REDIS_URL" ]; then
    echo "Error: REDIS_URL environment variable is not set"
    exit 1
fi

if [ "$SERVICE_TYPE" = "web" ]; then
    echo "Starting Flask application..."
    python app.py --port ${PORT:-5000}
elif [ "$SERVICE_TYPE" = "worker" ]; then
    echo "Starting Celery worker..."
    celery -A app.celery worker --loglevel=info
else
    echo "Please set SERVICE_TYPE to 'web' or 'worker'"
    exit 1
fi
