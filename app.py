import json
import schedule
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def whatever():
    data = json.loads(request.data)
    print(data);
    return data
