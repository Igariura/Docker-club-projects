import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'service': 'app1', 'message': 'I am App 1!'})

@app.route('/ping-app2')
def ping_app2():
    # app1 talks to app2 using its container NAME not IP
    response = requests.get('http://app2:5000/')
    return jsonify({
        'from': 'app1',
        'message_to_app2': 'Hey App2, are you there?',
        'app2_responded_with': response.json()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)