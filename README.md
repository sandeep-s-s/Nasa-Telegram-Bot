# NASA telegram bot [No-longer maintained]


This bot integrate some NASA apis to telegram client.

  - [NASA api] - NASA rest APIs for developers
  - [Telegram bot apis] - Telegram bot APIs for developers


# Features!
  -  /picoftheday command gives astronomy picture of the day 

### Tech

* [Python3] - Programming language 
* [Flask] - Python Framework




### Installation

* This app requires [python](https://www.python.org/) v3+ to run.
* For running applicaton on localhost , it need a ngrok server assistance which make your localhost available online
* Set webhook using link https://api.telegram.org/botYour_Api_Key/setWebhook?url=https://your-url.com/

Install the dependencies and devDependencies and start the server.

```sh
$ cd Nasa-Telegram-Bot
$ pip3 install pipenv
$ pipenv shell
$ pipenv install -r ./requirements.txt
$ export FLASK_APP=app.py
$ flask run
```

### For demo 
[Demo bot](http://t.me/qwerty_quote_bot) - This telegram bot available till Wednesday 21 October 2020`

[NASA api]: <https://api.nasa.gov/>
[Telegram bot apis]: <https://core.telegram.org/bots>
[Flask]: <https://flask.palletsprojects.com/>
[Python3]: <https://www.python.org/>


