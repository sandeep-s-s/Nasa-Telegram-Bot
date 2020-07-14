from flask import Flask
import requests
from flask import request
app = Flask(__name__)

api_key = 'Your api key'
api_url = 'https://api.telegram.org/bot'


@app.route('/get-bot-info')
def botInfo():
    return("hello sandeep");


@app.route('/')
def index():
    res = requests.get(api_url+api_key+'/getUpdates')
    message = res.json()['result'][0]
    chat_id,text = getMessage(message)
    response = requests.post(api_url+api_key+"/sendMessage",json=sendMessage(chat_id))
    #import pdb; pdb.set_trace()
    return  response.json()

def sendMessage(chat_id):
    query_string = {"text" :"Hello man","chat_id":chat_id}
    return query_string

def getMessage(message):
    chat_id = message['message']['chat']['id'] 
    text = message['message']['text']
    return chat_id,text

if __name__ == "__main__":
    app.run(debug=True)
