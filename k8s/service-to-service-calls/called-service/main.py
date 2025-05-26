from flask import Flask
from datetime import datetime
import pytz
import argparse

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/home')
def home():
    ist_timezone = pytz.timezone('Asia/Kolkata')
    ist_time = datetime.now(ist_timezone).strftime("%I:%M %p")
    return f"hello world, current time is {ist_time}"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=args.port)
