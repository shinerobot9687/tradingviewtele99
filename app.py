import json
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/webhook', methods=['POST'])
def whatever():
    print(request.data)
    data = json.loads(request.data)

    return {
        "code": "success",
        "message": data
    }