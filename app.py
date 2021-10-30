import json
from flask import Flask, request, render_template
app = Flask(__name__)

symData = [];

@app.route('/')
def welcome():
    return render_template('index.html', symData)

@app.route('/webhook', methods=['POST'])
def whatever():
    
    data = json.loads(request.data)

    symData[0] = data['exchange'];
    symData[1] = data['price'];
    symData[2] = data['volume'];
    symData[3] = data['time'];
    return {
        "code": "success",
        "message": data
    }