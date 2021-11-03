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
    requestData = request.data;
    print(requestData);
    readData = json.loads(requestData.replace("'", "\""))
    chk = False;
    chkk = False;
    global coinName
    for keyread in readData.keys():
        if keyread == 'arbitrage':
            chk = True
        if keyread == 'exchange':
            chkk = True
    
    if chk == True:
        coinName = readData['arbitrage'].split(',')
        coinName.pop();
        print('Read OK',coinName);
        

    elif chkk == True:
        global coinSym

        if coinSym:
            check = False;
            coinSymRead = readData['exchange'];
            for coin in coinSym.keys():
                if coin == coinSymRead:
                    check = True;
                    break;
            
            if check == True:
                if coinSym[coinSymRead] >= 1:
                    coinSym[coinSymRead] = 0

                    totalString = readData['name']+' | 코인 : ' + readData['exchange'] + ' 거래량 : ' + str(readData['volume']) + ' 금액 : ' + str(readData['price']) + ' 시간 : ' + str(readData['time'])

                    checkarrow = ""
                    for keyread in coinName:    
                        if keyread in readData['exchange']:
                            checkarrow  = '✅ ' #'✅ '+ readData['name']+' | 코인 : ' + readData['exchange'] + ' 거래량 : ' + str(readData['volume']) + ' 금액 : ' + str(readData['price']) + ' 시간 : ' + str(readData['time'])
                    
                    #time.sleep(5)

                    bot = telegram.Bot(token='2075219807:AAGv_N_NmKXAie0F-bhzOR8woQ7QV-W-_7Y')
                    chat_id = '@cryptotradingviewconnect'
                    bot.sendMessage(chat_id=chat_id, text=totalString)
                    chat_id = '1000903796'
                    bot.sendMessage(chat_id=chat_id, text=(checkarrow + totalString))

                    print('send',totalString)
                elif coinSym[coinSymRead] < 1:
                    coinSym[coinSymRead] = coinSym[coinSymRead] + 1
                    print('sum', coinSym[coinSymRead],coinSymRead)

            else:
                coinSym.update({coinSymRead : 1})
                print('add', coinSym[coinSymRead], coinSymRead)
                
        else:
            coinSym = {readData['exchange'] : 1}
            print('add', coinSym[readData['exchange']],readData['exchange'])
        
        

    #totalString = readData['name']+' 종목 : ' + readData['exchange'] + ' 거래량 : ' + str(readData['volume']) + ' 금액 : ' + str(readData['price'])

    #bot = telegram.Bot(token='2075219807:AAGv_N_NmKXAie0F-bhzOR8woQ7QV-W-_7Y')
    #chat_id = '@cryptotradingviewconnect'
    #bot.sendMessage(chat_id=chat_id, text=totalString)
    #bot.sendMessage(chat_id=1000903796, text=totalString)

    #print("chk",readData)
    return {
        "code": "succss",
        "message": readData
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)