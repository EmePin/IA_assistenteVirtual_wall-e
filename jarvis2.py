import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.say("¿Cómo te llamas?")
engine.runAndWait()


def talk(text):
    '''
        here, virtual assistant can talk
    '''
    engine.say('Hola'+text)
    engine.runAndWait()


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
        print(rec)
        talk(rec)

except:
    pass
