# filepath: /home/ubaid/k8splayground/prometheus-container-metrics/service1/main.py

from flask import Flask, request
import prometheus_client
from prometheus_client import Counter, Gauge
import click
import random

# Initialize Flask app
app = Flask(__name__)

# Initialize Prometheus metrics
REQUESTS = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
RANDOM_GAUGE = Gauge('random_value', 'A random value that can be updated')

# Initialize gauge with a random value between 0 and 100
RANDOM_GAUGE.set(random.uniform(0, 100))

@app.route('/')
def hello():
    # Increment the request counter
    REQUESTS.labels(method='GET', endpoint='/').inc()
    return 'Hello, World!'

@app.route('/update_gauge', methods=['POST'])
def update_gauge():
    # Increment the request counter
    REQUESTS.labels(method='POST', endpoint='/update_gauge').inc()

    # Get value from request if provided
    try:
        value = request.args.get('value')
        if value is not None:
            RANDOM_GAUGE.set(float(value))
        else:
            RANDOM_GAUGE.set(random.uniform(0, 100))
        return {'status': 'success', 'current_value': float(RANDOM_GAUGE._value.get())}
    except ValueError:
        return {'status': 'error', 'message': 'Invalid value provided'}, 400

@click.command()
@click.option('--app-port', default=5000, help='Port for the Flask application')
@click.option('--metrics-port', default=9090, help='Port for Prometheus metrics')
def main(app_port, metrics_port):
    # Enable default prometheus metrics (process and python metrics)
    prometheus_client.start_http_server(metrics_port)
    # Run the Flask app
    app.run(host='0.0.0.0', port=app_port)

if __name__ == '__main__':
    main()