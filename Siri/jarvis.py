import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia

name = 'siri'
key = 'AIzaSyDT8oXpGz-zPCkNhHd_ELK8Gbwc65RcmSM'
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
    except:
        pass
    return rec

def run():
    rec = listen()
    if 'play' in rec:
        music = rec.replace('play', '')
        talk('Playing ' + music)
        pywhatkit.playonyt(music)
    elif 'how many subscribers does the channel have' in rec:
        name_subs = rec.replace('how many subscribers does the channel have', '').strip()
        data = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=' + name_subs + '&key=' + key).read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        talk(name_subs + " have {:,d}".format(int(subs)) + " subscribers! ")
    elif 'time' in rec:
        time = datetime.datetime.now().strftime('%H:%M %p')
        talk('It is ' + time)
    elif 'search' in rec:
        order = rec.replace('search', '')
        info = wikipedia.summary(order, 1)
        talk(info)
    else:
        talk("Retry")
while True:
    run()
run()