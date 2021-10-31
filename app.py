import os
import json
import requests
from flask import Flask, request, render_template
app = Flask(__name__)

def send_message(msg):
    url='https://hooks.slack.com/services/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'
    data = {'text':msg}
    resp = requests.post(url=url, json=data)

@app.route('/',methods=['GET'])
def welcome():
    return render_template('index.html')

@app.route('/webhook',methods=['POST'])
def whatever():
    readData = json.loads(request.data)

    totalString = '종목 : ' + readData['exchange'] + '거래량 : ' + readData['volume'] + '금액 : ' + readData['price']

    send_message(totalString)
    
    print(readData)
    return {
        "code": "succss",
        "message": readData
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)