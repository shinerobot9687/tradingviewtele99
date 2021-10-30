import json

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def whatever():
    data = json.loads(request.data)

    if data['passphrase'] != config.WEBHOOK_PASSPHRASE:
        return{
            "code": "error",
            "message": "Nice try, invalid passphrase"
        }

    print(data);
    return {
        "code": 'success',
        "message": data
    }
