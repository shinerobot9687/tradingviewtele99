import json
import requests
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def welcome():
    return render_template('index.html')

@app.route('/webhook',methods=['GET','POST'])
def whatever():
    readData = json.loads(request.data)
    return {
        "code": "succss",
        "message": readData
    }