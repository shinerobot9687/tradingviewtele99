#실행 flask run

#-*- coding:utf-8 -*-



import os
import json
import telegram
from flask import Flask, request, render_template
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)
coinSym = {}
coinName =[]

@app.route('/',methods=['GET', 'OPTIONS'])
def welcome():
    return render_template('index.html')

@app.route('/webhook',methods=['POST'])
def whatever():
    
    readData = json.loads(request.data)
    print('read OK',readData);

    #bot = telegram.Bot(token='2075219807:AAGv_N_NmKXAie0F-bhzOR8woQ7QV-W-_7Y')
    #chat_id = '-1001155984303'
    #bot.sendMessage(chat_id=chat_id, text=(readData))    

    #readData=""

      
    return {
        "code": "succss",
        "messge": readData
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

#  bot = telegram.Bot(token='2075219807:AAGv_N_NmKXAie0F-bhzOR8woQ7QV-W-_7Y')
# chat_id = '-1001155984303'
# bot.sendMessage(chat_id=chat_id, text=("ddsds"))