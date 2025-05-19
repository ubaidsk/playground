from flask import Flask
from datetime import datetime
import pytz
import signal
import sys

app = Flask(__name__)

def signal_handler(sig, frame):
    print('Received shutdown signal, gracefully exiting...')
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

@app.route("/")
def hello_world():
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    return f"<p>Hello, World! Current time in IST is {current_time}</p>"

@app.route("/health")
def health():
    return "<p>Health check: OK</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
