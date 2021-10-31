import json
#import requests
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')


app.run(host='0.0.0.0', port=8000) if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000")
    app.run(host="0.0.0.0", port=port)