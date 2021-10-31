import json
import requests
from flask import Flask, request, render_template
app = Flask(__name__)

#coinInfo ={}

@app.route('/')
def welcome():
    #data = {"exchange":"FTX",  "price": "1000",  "volume": "6442.4186", "time":"2021-10-30T11:59:18Z"}
    return render_template('index.html')

    #return render_template('dddd.html')
    
#app.run()

#if request.method == 'POST':
#        data = json.loads(request.data)
#        return {
#            "code": 'success',
#            "message": data
#        }
#    else:
#        return 
