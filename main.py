import pyttsx3                   #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime
import wikipedia                 #pip install wikipedia
import webbrowser
import os
import smtplib


print ("Initialising Jarvis")

MASTER = "Sir"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning"+MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon"+MASTER)
    else:
        speak("Good Evening"+MASTER)
    speak ("Hi I am Jarvis. How may I help you?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening...")
        audio = r.listen(source)

    try:
        print ("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print (f"user said: {query}\n")
    except Exception as e:
        print ("Please say again...")
        query = None
    return query

def sentmail (to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login ('email@gmail.com','password')
    server.sendmail('you@gmail.com',to,content)
    server.close()

#main program starts
def main():
    speak ("Initialising Jarvis...")
    wishme()
    query = takecommand()

    #logic for executing tasks as per query
    if 'wikipedia' in query.lower():
        speak ('Searching wikipedia...')
        query = query.replace("wikipedia","")
        result = wikipedia.summary(query, sentences=2)
        print (result)
        speak(result)
    elif 'open youtube' in query.lower():
        webbrowser.open("youtube.com")

    elif 'open google' in query.lower():
        webbrowser.open("google.com")    

    elif 'open linkedin' in query.lower():
        webbrowser.open("linkedin.org")

    elif 'open gmail' in query.lower():
        webbrowser.open("gmail.com")
    elif 'open nptel' in query.lower():
        webbrowser.open("https://swayam.gov.in/nc_details/NPTEL")
    elif 'open facebook' in query.lower():
        webbrowser.open("facebook.com")
    elif 'open hotstar' in query.lower():
        webbrowser.open("hotstar.com")
    elif 'play music' in query.lower():
        songs_dir = "D:\Music"
        songs = os.listdir(songs_dir)
        print (songs)
        takecommand()
        os.startfile(os.path.join(songs_dir,songs[1]))
    elif 'the time' in query.lower():
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strtime}")
    elif 'open code' in query.lower():
        codepath = "C:\\Users\\{user name}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
    elif 'email to you' in query.lower():
        try:
            speak('what should I sent?')
            content = takecommand()
            to = "you@gmail.com"
            sentmail(to,content)
            speak("Email has been sent succesfully...")
        except Exception as e:
            print (e)
    # You can add more things in this code after this by following the same method.
main()
