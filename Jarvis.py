import re
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('sbodani82@gmail.com', 'your_password')
    server.sendmail('sbodani82@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
   # if 1:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)



        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open GitHub' in query:
            webbrowser.open("GitHub.com")

        elif 'open Gmail' in query:
            webbrowser.open("Gmail.com")

        elif 'open Instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open Synthesis' in query:
            webbrowser.open("portal.synthesis.is")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open Spotify' in query:
            spotifyPath = "C:\\Users\\Shreyas\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotifyPath)

        elif 'open chrome' in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif 'open Firefox' in query:
            firefoxPath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(firefoxPath)

        elif 'open Terminal' in query:
            terminalPath = "%windir%\\system32\\cmd.exe"
            os.startfile(terminalPath)

        elif 'open Scratch' in query:
            scratchPath = "C:\\Program Files (x86)\\Scratch 3\\Scratch 3.exe"
            os.startfile(scratchPath)
        
        elif 'email to Dad' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "....."
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I was not able to send this email")

        elif 'email to Mom' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "...."
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I was not able to send this email")

