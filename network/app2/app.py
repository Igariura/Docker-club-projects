from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'service': 'app2', 'message': 'I am App 2! App1 can see me!'})

@app.route('/ping-app1')
def ping_app1():
    # app2 talks to app1 using its container NAME
    import requests
    response = requests.get('http://app1:5000/')
    return jsonify({
        'from': 'app2',
        'message_to_app1': 'Hey App1, are you there?',
        'app1_responded_with': response.json()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)