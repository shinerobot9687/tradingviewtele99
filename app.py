import os
import json
import requests
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/',methods=['GET'])
def welcome():
    return render_template('index.html')

@app.route('/webhook',methods=['POST'])
def whatever():
    readData = json.loads(request.data)

    totalString = '종목 : ' + readData['exchange'] + '거래량 : ' + readData['volume'] + '금액 : ' + readData['price']

    requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+"xoxb-1601840097190-1605530619493-lvOwi9vuMfRXdJ7rXm9T1god"},
    data={"channel": "#stock","text": totalString})
    print(readData)
    return {
        "code": "succss",
        "message": readData
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)