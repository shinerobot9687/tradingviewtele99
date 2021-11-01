#-*- coding:utf-8 -*-

import os
import json
import telegram
from flask import Flask, request, render_template
app = Flask(__name__)

coinSym = {}

@app.route('/',methods=['GET'])
def welcome():
    return render_template('index.html')

@app.route('/webhook',methods=['POST'])
def whatever():
    readData = json.loads(request.data)

    global coinSym

    if coinSym:
        check = False;
        coinSymRead = readData['exchange'];
        for coin in coinSym.keys():
            if coin == readData['exchange']:
                check = True;
                break;
        
        if check == True:
            if coinSym[coinSymRead] >= 1:
                coinSym[coinSymRead] = 0
                #print("reset",coinSym)

                totalString = readData['name']+' 종목 : ' + readData['exchange'] + ' 거래량 : ' + str(readData['volume']) + ' 금액 : ' + str(readData['price'])

                bot = telegram.Bot(token='2075219807:AAGv_N_NmKXAie0F-bhzOR8woQ7QV-W-_7Y')
                chat_id = '@cryptotradingviewconnect'
                bot.sendMessage(chat_id=chat_id, text=totalString)
                bot.sendMessage(chat_id=1000903796, text=totalString)

                print('send',coinSym[coin], totalString)
            else:
                coinSym[coinSymRead] = coinSym[coinSymRead] + 1
                print(coinSym[coinSymRead],readData)
        else:
            coinSym[coinSymRead] = coinSym[coinSymRead] + 1
            print(coinSym[coinSymRead], readData)

    else:
        coinSym = {readData['exchange'] : 1}
        print(coinSym, readData)
        

    #totalString = readData['name']+' 종목 : ' + readData['exchange'] + ' 거래량 : ' + str(readData['volume']) + ' 금액 : ' + str(readData['price'])

    #bot = telegram.Bot(token='2075219807:AAGv_N_NmKXAie0F-bhzOR8woQ7QV-W-_7Y')
    #chat_id = '@cryptotradingviewconnect'
    #bot.sendMessage(chat_id=chat_id, text=totalString)
    #bot.sendMessage(chat_id=1000903796, text=totalString)

    print(readData)
    return {
        "code": "succss",
        "message": readData
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)