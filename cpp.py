
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import python_weather
import os
import sys
import smtplib


listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def say(audio):
   engine.say(audio)
   engine.runAndWait()
    
def wishme():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
      say("Good morning")
      print("good morning")
   elif hour>=12 and hour<18:
      say("good evening")
      print("good evening")
   else:
      say("good night");
      print("good night")

   say("i am ACE ")
   print ("i am ACE ")
   

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'ACE' in command:
                command = command.replace('ACE', '')
                print(command)
    except Exception as e:
        say("Say that again...")
        print("Say that again...")
        return "none"
    return command
   
def send_email(to,subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('maskedclown33@gmail.com', 'cakk zrbn bubk wwyj')
    #message = f"Subject: {subject}\n\n{body}"
    server.sendmail('maskedclown33@gmail.com', to,subject, content)
    server.close()

def run_ACE():
    command = take_command()
    print(command)
    
    if 'play' in command:
        song = command.replace('play', '')
        say('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        say('Current time is ' + time)
    elif ' wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 1)
        print(info)
        say(info)
    elif 'date' in command:
        say('sorry, I have a headache')
    elif 'who are you' in command:
        say('I am an Artificial Conversation entity and I was developed by MANAS , SHOUNAK , YASHVARDHAN  , SIDDESH  ')
        print('I am an Artificial Conversation entity and I was developed by MANAS , SHOUNAK , YASHVARDHAN  , SIDDESH  ')
    elif 'are you single' in command:
        say('I am in a relationship with wifi')
        print('I am in a relationship with wifi')
    elif 'joke' in command:
        say(pyjokes.get_joke())
    elif 'open stack overflow' in command:
        webbrowser.open("stackoverflow.com")
    elif 'open youtube' in command:
        webbrowser.open("youtube.com")
    elif 'open google' in command:
        webbrowser.open("google.com")
        
    elif 'open notepad' in command:
        path =("C:\\Windows\\system32\\Notepad.exe")
        os.startfile(path)
    elif 'close notepad' in command:
        os.system("taskkill /f /im notepad.exe")
        say("Notepad is close")
    elif 'open vs code' in command:
        path =("D:\\Microsoft VS Code\\Code.exe")
        os.startfile(path)
    elif 'send mail' in command:
        try:
           #say("whom should i send")
           #to=take_command().lower()
          # print(to)
           say("what subjects should be mentioned")
           subject=take_command().lower()
           say("what should i say")
           content=take_command().lower()
           to="shounakdighe@gmail.com","jadhav.yashvardhan5@gmail.com","nikita07gaikwad@gmail.com"
           print(subject)
           print(content)
           send_email(to,content)
           say("email has been sent")
        except Exception as e:
           print(e)
    elif 'ACE stop' in command:
       say("thanks for using me")
       sys.exit()
    else:
        say('Please say the command again.')
    say("do you have any other work")

wishme()
while True:
    run_ACE()
    
    
