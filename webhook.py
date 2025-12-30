from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/webhook', methods=['GET'])
def verify():
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if token == "PensayFlowerToken123!":
        return challenge, 200
    return 'Forbidden', 403

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print('Message received:', data)
    return 'OK', 200

@app.route('/')
def home():
    return 'Running!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))