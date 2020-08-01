from flask import Flask
import requests
from flask import request
from config import nasa_token,telegram_token,nasa_url,telegram_url;
app = Flask(__name__)


@app.route('/get-bot-info')
def botInfo():
    response = requests.get(telegram_url+telegram_token+"/getMe")
    return  response.json()

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        message = request.get_json()
        chat_id,text = getMessage(message)
        response = requests.post(telegram_url+telegram_token+"/sendPhoto",json=sendMessage(chat_id,text))
        return  response.json()
    else:
        return "Something went wrong !!"

def sendMessage(chat_id,text):
    if(text=='/picoftheday'):
        response = requests.get(nasa_url+'?api_key='+nasa_token)
        return {"caption" :"<b>"+response.json()['title']+"</b>\n"+response.json()['explanation'],"chat_id":chat_id,"photo":response.json()['url'],"parse_mode":"html"}
    else:
        return  {"text" :text,"chat_id":chat_id}

def getMessage(message):
    chat_id = message['message']['chat']['id']
    text = message['message']['text']
    return chat_id,text

if __name__ == "__main__":
    app.run(debug=True)
