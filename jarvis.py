import cv2
import kit
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import cv2
import pywhatkit as wk
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import sys
import pyjokes
import pyautogui
import time
import main
import instaloader
from pytube import Search
import platform







# Initialize the TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return None

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        speak("I couldn't understand what you said. Please try again.")
        return None
    except sr.RequestError:
        speak("Could not request results; check your network connection.")
        return None
    except Exception as e:
        print(e)
        speak("Say that again, please...")
        return None


def news():
    main_url ='https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3ff5d007fbf14110adb39dec76f254e7'
    main_page=requests.get(main_url).json()
    articles=main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's{day[i]} news is:{head[i]}")


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning")
    elif hour>12 and hour<18:
        speak("Good afternoon ")
    else: speak("Good evening")
    speak("I am Jarvis mam. please tell me how can i help you ")
# def news():
#     main_url = 'https://newsapi.org/v2/rop.headlines?sources=techrunch&apiKey=3ff5d007fbf14110adb39dec76f254e7'
#     main_page = requests.get(main_url).json()
#
#     articles=main_page["articles "]
#     head=[]
#     day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
#     for ar in articles:
#         head.append(ar["title"])
#     for i in range(len(day)):
#         speak(f"taday's {day[i]} news is: {head[i]}")




def open_vscode(path=""):
    system_platform = platform.system()

    if system_platform == "Windows":
        os.system(f'start code {C:\\Users\\shiva\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code}')
    elif system_platform == "Darwin":  # macOS
        os.system(f'open -a "Visual Studio Code" {C:\\Users\\shiva\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code}')
    elif system_platform == "Linux":
        os.system(f'code {C:\\Users\\shiva\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code}')
    else:
        print(f"Unsupported platform: {system_platform}")


if __name__ == "__main__":

    wish()
    while True:
    # if 1:
        query=takecommand().lower()
        if "jarvis wake up" in query:
            print("yes sir")
            speak("yes sir")

        elif "who are you" in query:
            print("My name is Jarvis")
            speak("My name is Jarvis")
            print(" i can do Everything that my creator programed me to do")
            speak(" i can do Everything that my creator programed me to do")

        elif ("open command prompt") in query:
            os.system("start cmd")
        elif "Open Camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"your IP address is{ip}")
        elif "wikipedia" in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=5)
            speak("According to wikipedia")
            speak(results)
            print(results)
        elif " just open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open linkedin" in query:
            webbrowser.open("www.linkedin.com")
        elif "open github" in query:
            webbrowser.open("www.github.com")
        elif "open my gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
        elif "open google" in query:
            speak("sir,what should i search on google")
            qry=takecommand().lower()
            webbrowser.open(f"{qry}")
            results=wikipedia.summary(qry,sentences=1)
            speak(results)
        elif "send massege" in query:
            kit.sendwhatmsg("+917398616219","Hello",20,41)
        elif "open youtube" in query:
            speak("what you will like to watch?")
            qrry=takecommand().lower()
            wk.playonyt(f"{qrry}")
        elif "search on youtube" in query:
            query=query.replace("search on youtube","")
            webbrowser.open(f"www.youtube.com/result/search_query{query}")

        elif "no thanks" in query:
            speak("thanks for using me sir,have a good day")
            sys.exit()

        elif "tell me a joke  " in query.lower():

            joke=pyjokes.get_joke(language='en')
            speak(joke)
        elif "shut down the system" in query:
            os.system("shutdown /s /t s")
        elif "restart the system" in query:
            os.system("shutdown /r /t s")
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif "tell me news" in query:
            speak("please wait sir,fetching the latest news")
            news()
        elif "where i am" in query or "where we are" in query:
            speak("wait sir,let me check")
            try:
                ipAdd= requests.get('https://api.ipify.org').text
                print(ipAdd)
                url='https://get.geojs.io/v1/ip/geo'+ipAdd+'.json'
                geo_requests=requests.get(url)
                geo_data=geo_requests.json()
                city=geo_data['city']
                country=geo_data['country']
                speak(f"sir i am not sure,but i think we are in {city} city of{country} country")
            except Exception as e:
                speak("sorry sir,due to network issues i am not able to find where we are.")
                pass
        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir please enter the user name correctally")
            name=input("enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir would you like to download profile picture of this account.")
            condition =takecommand().lower()
            if "yes" in condition:
                mod=instaloader.Instaloader()
                mod.download_profile(name,profile_pic_only=True)
                speak("i am done sir,profile picture is saved in our main folder .now i am ready")
            else:
                pass
        elif "take screenshot" in query or"take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name=takecommand().lower()
            speak("please sir hold the screenshot for few seconds,i am taking screenshot")
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir,the screenshot is saved in our folder .now i am ready for other work")
        elif "play music" in query:
            music_dir="C:\\Users\\shiva"
            songs=os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir,song))
        elif "open  vs code" in query:
              open_vscode()



        speak("sir,do you have any other work")


