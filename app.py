import json

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    data = {"exchange":"FTX",  "price": "1000",  "volume": "6442.4186", "time":"2021-10-30T11:59:18Z"}
    return render_template('index.html', symread = data)

@app.route('/webhook', methods=['POST','GET'])
def whatever():
    

    if request.method == 'POST':
        data = json.loads(request.data)
        return {
            "code": 'success',
            "message": data
        }
    else:
        return render_template('index.html', symread = data)
    
