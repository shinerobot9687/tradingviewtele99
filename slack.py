import requests

token = "xoxb-1601840097190-1605530619493-lvOwi9vuMfRXdJ7rXm9T1god"
channel = "#stock"
text = "Check your stock crawler."


requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": text})