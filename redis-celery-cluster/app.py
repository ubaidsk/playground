from flask import Flask, request, jsonify
from celery import Celery
import os
import click

def get_redis_url():
    redis_url = os.environ.get('REDIS_URL')
    if not redis_url:
        raise ValueError("REDIS_URL environment variable must be set")
    return redis_url

# Get Redis URL first
redis_url = get_redis_url()

# Initialize Flask and Celery with proper broker URL
app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = redis_url

celery = Celery(app.name, broker=redis_url)
celery.conf.update(
    worker_send_task_events=True,
    task_send_sent_event=True
)

@app.route('/')
def index():
    return "Welcome to the Celery Redis Cluster Example!"

@celery.task
def send_email(recipient):
    # Simulate email sending
    import time
    time.sleep(5)
    return f'Email sent to {recipient}'

@app.route('/send-email', methods=['POST'])
def send_email_route():
    data = request.get_json()
    recipient = data['recipient']
    task = send_email.delay(recipient)
    return jsonify({ 'task_id': task.id }), 202

@app.route('/status/<task_id>')
def task_status(task_id):
    task = send_email.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {'state': task.state, 'status': 'Pending...'}
    elif task.state != 'FAILURE':
        response = {'state': task.state, 'result': task.result}
    else:
        response = {'state': task.state, 'status': str(task.info)}
    return jsonify(response)

@click.command()
@click.option('--port', default=5000, help='Port to run the Flask application')
def main(port):
    """Run the Flask application on the specified port."""
    app.run(debug=False, host='0.0.0.0', port=port)

if __name__ == '__main__':
    main()