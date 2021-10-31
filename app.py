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

    url='https://hooks.slack.com/services/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'
    data = {'text':totalString}
    requests.post(url=url, json=data)

    print(readData)
    return {
        "code": "succss",
        "message": readData
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)