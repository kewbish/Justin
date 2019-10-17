import requests
import pyttsx3


def getInsult():
    url = ("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    response = requests.get(url)
    return response.json()['insult']


engine = pyttsx3.init()
engine.setProperty('volume', 1)
try:
    while True:
        insult = getInsult()
        engine.say(insult)
        engine.runAndWait()
except KeyboardInterrupt:
    engine.stop()
    print("Creation bests its master, eh?")
