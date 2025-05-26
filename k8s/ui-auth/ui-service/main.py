from flask import Flask
import ssl
from datetime import datetime
import pytz

app = Flask(__name__)

context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_SERVER)
# Load the server's certificate and private key
context.load_cert_chain('../certs/server.crt', '../certs/server.key')

@app.route("/")
def hello_world():
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    return f"<p>Hello, World! Current time in IST is {current_time}</p>"

@app.route("/health")
def health():
    return "<p>Health check: OK</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context=context)
