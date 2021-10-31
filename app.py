import json
import requests
from flask import Flask, request, render_template
app = Flask(__name__)




coinInfo ={}

@app.route('/')
def welcome():
    #data = {"exchange":"FTX",  "price": "1000",  "volume": "6442.4186", "time":"2021-10-30T11:59:18Z"}
    return render_template('index.html')

@app.route('/webhook',methods=['POST'])
def whatever():
    readData = json.loads(request.data)
    #coinInfo = {readData['exchange'] : 1}
    global coinInfo
    
    if coinInfo:
        for i in coinInfo.keys():
            if readData['exchange'] == i:
                checkBool = True
                break
            else : 
                checkBool = False
        
        if checkBool == True:
            coinInfo[i] = coinInfo[i] + 1
                
        elif checkBool == False:
            coinInfo.update({readData['exchange'] : 1})
    else:
        coinInfo = {readData['exchange'] : 1}
        
    totalString = '종목 : ' + readData['exchange'] + '거래량 : ' + readData['volume'] + '금액 : ' + readData['price']

    requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+"xoxb-1601840097190-1605530619493-lvOwi9vuMfRXdJ7rXm9T1god"},
    data={"channel": "#stock","text": totalString})

    
    return {
        "code": "succss",
        "message": readData
    }
    #return render_template('dddd.html')
    
app.run()

#if request.method == 'POST':
#        data = json.loads(request.data)
#        return {
#            "code": 'success',
#            "message": data
#        }
#    else:
#        return 
