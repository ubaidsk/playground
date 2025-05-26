FROM python:3.13-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY main.py .

# Expose ports for Flask and Prometheus metrics
EXPOSE 5000 9090

CMD ["python", "main.py"]
