#-*- coding:utf-8 -*-

import os
import json
import telegram
from flask import Flask, request, render_template
app = Flask(__name__)


    
    

@app.route('/',methods=['GET'])
def welcome():
    

    return render_template('index.html')

@app.route('/webhook',methods=['POST'])
def whatever():
    readData = json.loads(request.data)

    totalString = '종목 : ' + readData['exchange'] + ' 거래량 : ' + str(readData['volume']) + ' 금액 : ' + str(readData['price'])

    bot = telegram.Bot(token='2075219807:AAGv_N_NmKXAie0F-bhzOR8woQ7QV-W-_7Y')
    chat_id = 1000903796
    bot.sendMessage(chat_id=chat_id, text=totalString)
    

    print(readData)
    return {
        "code": "succss",
        "message": readData
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)