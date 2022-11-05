import speech_recognition as sr
import pyttsx3
import pywhatkit

def talk(command):
    engine = pyttsx3.init()
    voice = engine.getpropety('voices')
    engine.setProperty('voice',voice[1].id)
    engine.say("playing"+command)
    engine.runAndWait()

def takecommand():
    listener=sr.Recognizer()
    try:
        with sr.Microphone() as source:
         print("listening...")
         voice=listener.listen(source)
         command=listener.recognize_google(voice)
         

         talk(command)
         pywhatkit.playonyt(command)

    except:
        pass

takecommand()
talk()
