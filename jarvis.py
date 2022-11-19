'''
    Description:
    Create your own virtual assistant with python.
    Author: Aimée
    Version: 1.1
    Video base: https://youtu.be/8WKjX0dbh4E
'''
import pyjokes
import AVMSpeechMath as sm
import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia

# name of the virtual assistant
name = 'maya'



# the flag help us to turn off the program
flag = 1

listener = sr.Recognizer()

engine = pyttsx3.init()

# get voices and set the first of them
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# editing default configuration
engine. setProperty('rate', 178)
engine.setProperty('volume', 0.7)


def talk(text):
    '''
        here, virtual assistant can talk
    '''
    engine.say(text)
    engine.runAndWait()


def listen():
    '''
        The program recover our voice and it sends to another function
    '''
    flag = 1
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()

            if name in rec:
                rec = rec.replace(name, '')
                flag = run(rec)
            else:
                talk("Vuelve a intentarlo, no reconozco: " + rec)
    except:
        pass
    return flag


def run(rec):
    '''
        All the actions that virtual assistant can do
    '''
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)
    
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        wikipedia.set_lang("es")
        info = wikipedia.summary(order, 1)
        talk(info) 
    elif 'chiste' in rec:
        chiste = pyjokes.get_joke("es")
        talk(chiste)
    # elif 'suma' in rec:
    #     talk(sm.getResult(rec))
    elif 'adiós' in rec:
        flag = 0
        talk("Nos vemos...") 
    else:
        talk("Vuelve a intentarlo, no reconozco: " + rec)
    return flag


while flag:
    flag = listen()
