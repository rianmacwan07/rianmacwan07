from random import random
import pyttsx3
import speech_recognition as SR
import datetime
import pywhatkit
import os
import webbrowser

engine = pyttsx3.init('sapi5')
voice = engine.getpropety('voices')
engine.setProperty('voice',voice[1].id)

def speak(audio):
    engine.say(audio)

    engine.runAndWait()

def definename(self,Newname):
    self.Newname = Newname
    speak("please tell me your name")
    Newname = takecommand()
    speak(f"is your name {Newname}")
    speak("is it correct?")
    correction = takecommand()
    if 'yes' in correction:
      self.name = Newname
      speak(f"hello {Newname} how you doin?")
    else:
        speak("please write your name i did not get that")
        name=input("enter your name")
        speak(f"hello {name} how you doin?")

def takecommand():
    r = SR.Recognizer()
    with SR.Microphone as source:
        print("hearing.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("recognizing.....")
        User = r.recognize_google(audio,language="en-in")
        print(f"user said {User}\n")

    except Exception as e:
        print("say that again please......")
        return "None"
    return User

def quotes_mood(self,User):
    quotes = random.randint(1,3)
    self.User = User
    self.User = takecommand()

    
    
    speak("what is your mood i can give tell you some quotes for sad,motivate,happy and family or i can tell you story")
    if self.User== "sad" in self.User:
      if quotes == 1:
         speak("i am A Good Man. But My Hands... These Hands Belong To The Devil.")
     
      elif quotes == 2:
        speak("Broke My F***ing Heart To Pull Her From The Cut.")
    
      elif quotes == 3:
        speak("There Is No Rest For Me In This World. Perhaps In The Next.")

    elif self.User == "motivate" in self.User:
      if quotes == 1:
        speak("she doesn't deserve what i am , she doesn't deserve what i will become")
      
      elif quotes == 2:
        speak("i know you are tired. i know you are physically and emotionally drained but you have to keep going")
      
      elif quotes == 3:
        speak("dont push me away and wonder where i went")
    
    elif self.User=="happy" in self.User:
      if quotes == 1:
        speak("Happiness is not the absence of problems, it’s the ability to deal with them.")

      elif quotes == 2:
        speak("It is not how much we have, but how much we enjoy, that makes happiness.")
      
      elif quotes == 3:
        speak("Happiness is not an ideal of reason, but of imagination")
    
    elif self.User == "family" in self.User:
        if quotes == 1:
            speak("to family sometimes it is the shelter from the storm sometimes it is the storm itself")

        elif quotes == 2:
            speak("Family can be more than just those with whom we share blood. We can choose.")
        
        elif quotes == 3:
            speak("the bond that links your true family is not one of blood, but of respect and joy in each other’s life")

    elif self.User == "story" in self.User :
        if quotes == 1:
            speak('''There was once a milkmaid named Patty.She milked her cow and carried the two pails of milk she fetched on a stick and set out to sell the milk at the market.
            As she was walking to the market, she began to daydream about what she would do with the money she got for the milk.
            She thought of buying a hen and selling its eggs and she planned on becoming wealthy.She dreamt of buying a cake, a basket of strawberries, a fancy dress, and even a new house with the money she would make selling the eggs and the milk!
            In her excitement, she forgot about the pails she was carrying and began to skip.Suddenly, she realised that the milk was spilling down and when she checked her pails, they were empty''')
            
        elif quotes == 2:
            speak('''An old man lived in the village. He was one of the most unfortunate people in the world. The whole village was tired of him; he was always gloomy, he constantly complained and was always in a bad mood
            The longer he lived, the more bile he was becoming and the more poisonous were his words. People avoided him, because his misfortune became contagious. It was even unnatural and insulting to be happy next to him
            He created the feeling of unhappiness in others
            But one day, when he turned eighty years old, an incredible thing happened. Instantly everyone started hearing the rumour
            “An Old Man is happy today, he doesn’t complain about anything, smiles, and even his face is freshened up.
            The whole village gathered together. The old man was asked
            Villager: What happened to you
            “Nothing special. Eighty years I’ve been chasing happiness, and it was useless. And then I decided to live without happiness and just enjoy life. That’s why I’m happy now.” – An Old Ma
            Moral of the story:
            Do not chase happiness. Enjoy your life''') 

        elif quotes == 3:
            speak(''' A story tells that two friends were walking through the desert. During some point of the journey they had an argument, and one friend slapped the other one in the face.
            The one who got slapped was hurt, but without saying anything, wrote in the sand;
            “Today my best friend slapped me in the face.”
            They kept on walking until they found an oasis, where they decided to take a bath. The one who had been slapped got stuck in the mire and started drowning, but the friend saved him. After he recovered from the near drowning, he wrote on a stone;
            “Today my best friend saved my life.”
            The friend who had slapped and saved his best friend asked him;
            “After I hurt you, you wrote in the sand and now, you write on a stone, why?”
            The other friend replied;
            “When someone hurts us we should write it down in sand where winds of forgiveness can erase it away. But, when someone does something good for us, we must engrave it in stone where no wind can ever erase it.”
            Moral of the story: 
            Don not value the things you have in your life. But value who you have in your life.
            ''') 
    

    speak(f" hello {self.name} how may i help you ")
    if self.name == definename():

        while True:

            voice_com = takecommand()

    if  'how are you ' in voice_com:

        speak(f'I am awesome thanks for asking {self.name}')

    elif 'about' in voice_com:

        speak('Hi i am my name is edith i am an Ai made by rian macwan and i can do many interesting things i am very useful and i can do many things')
        speak('i can talk to you')
        speak('i can do various work like play music,movies and also help you to see your codes')
        speak('i can send messages on whatsapp')
        speak('i can also tell you stories quotes')
        speak('i can tell the ccurrent time date and year')
        speak('i am als trying to be a greater verion of myself and i will try that to do in near by future')

    elif 'time' or 'date' or 'year' in voice_com:
        current_time = datetime.datetime.now().curtime("%H:%M:%S")
        speak(f'Sir the time is {current_time}')

    elif 'play song' in voice_com:
        speak('you want to listen your own songs or from external')
        choose = takecommand()

        if 'own' or 'my' in choose:
            speak('opening your songs')
            music = 'E:\music'
            songs=os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music,songs))

        elif 'youtube' in choose:
            speak("please tell me which song you want to listen")
            song = takecommand()
            speak(f'playing {song} on youtube')
            pywhatkit.playonyt(song)

        else:
            speak(f"i did not get the music {self.name}")
    
    elif 'open google' in voice_com:
        speak('opening google')
        webbrowser.open('google.com')

    elif 'open youtube' in voice_com:
        speak('opening youtube')
        webbrowser.open('youtube.com')

    #elif 'open code' in voice_com:
     #   code_way = 'C:\Users\DELL\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code'
      #  os.startfile(code_way)

    


        



