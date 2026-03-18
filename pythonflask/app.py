from flask import Flask, jsonify
import os, datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Hello from Dockerized Flask!',
        'time': str(datetime.datetime.now()),
        'environment': os.getenv('APP_ENV', 'development')
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)