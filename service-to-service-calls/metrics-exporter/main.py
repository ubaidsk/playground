from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route('/metrics')
def metrics():
    dummy_metric = {
        'metric_name': 'dummy_metric',
        'value': random.randint(0, 100),
        'timestamp': int(time.time())
    }
    return jsonify(dummy_metric)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)