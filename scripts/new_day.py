import requests
import datetime
from webbrowser import open
from os import startfile

key = '8f0f4a7f4957ee451a11d91cec116628'
now = datetime.datetime.now()


def current_weather():
    url = 'http://api.openweathermap.org/data/2.5/weather'
    query_params = {
        'q': 'Vancouver',
        'appid': key,
    }
    response = requests.get(url, params=query_params)
    return response.json()['weather'][0]['description']


def qotd():
    qotdjson = requests.get('https://quotes.rest/qod')
    return qotdjson.json()['contents']['quotes'][0]['quote']


def aotd():
    aotdjson = requests.get('https://quotes.rest/qod')
    return aotdjson.json()['contents']['quotes'][0]['author']


print("Welcome Master. It's currently the beautiful day that is " +
      now.strftime("%m-%d %H:%M:%S") + ".")
vanweather = current_weather()
print("On today's menu is some good " + vanweather + ".")
jesussaid = qotd()
somedude = aotd()
print("Jesus also called while you were asleep, he wants you to know that some " +
      somedude + " left a message saying \"" + jesussaid + "\".")
ans = input("You sure you've done everything? [Y / N] ")
if (ans == "n") or (ans == "N"):
    print("I think you gotta do that, y'know?")
else:
    print("Alright, opening tabs.")
    open("https://mail.google.com/mail/")
    open("https://discordapp.com/channels/@me")
    open("https://reddit.com")
    startfile(r"C:\Users\offic\Documents\Instagram.lnk")
