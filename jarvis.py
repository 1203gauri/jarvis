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
import random
import pyautogui as pi








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
        return query.lower()
    except sr.UnknownValueError:
        speak("I couldn't understand what you said. Please try again.")
        return None
    except sr.RequestError:
        speak("Could not request results; check your network connection.")
        return None


import subprocess
import pyautogui
import time
from urllib.parse import quote

import time



import pywhatkit as kit
import datetime

# Predefined contact list (Add your own numbers)
contacts = {
    "john": "+911234567890",
    "Varsha Di": "+91 92354 15290",
    "shiva": "+91782283717219"  # Add your contacts here
}

# def send_whatsapp_message():
#     """Sends a WhatsApp message using voice commands."""
#
#     speak("Who do you want to send a message to?")
#     name = takecommand()
#
#     if name is None or name.lower() not in contacts:
#         speak("Sorry, I don't have that contact. Please add it to my list.")
#         return
#
#     phone_number = contacts[name.lower()]
#
#     speak("What message should I send?")
#     message = takecommand()
#
#     if message is None:
#         speak("I didn't catch that. Please try again.")
#         return
#
#     # Get the current time
#     now = datetime.datetime.now()
#     hours, minutes = now.hour, now.minute + 2  # Schedule 2 minutes ahead
#
#     # Prevent invalid minute values (reset to 0 if exceeds 59)
#     if minutes >= 60:
#         minutes -= 60
#         hours += 1
#
#     # Ensure hours stay within 24-hour format
#     if hours >= 24:
#         hours = 0
#
#     # Send WhatsApp message
#     speak(f"Sending message to {name}: {message}")
#     kit.sendwhatmsg(phone_number, message, hours, minutes)
#
#     speak("Message has been sent successfully.")
def send_whatsapp_message():
    """Sends a WhatsApp message instantly and presses Enter to send."""

    speak("Who do you want to send a message to?")
    name = takecommand()

    if name is None or name.lower() not in contacts:
        speak("Sorry, I don't have that contact. Please add it to my list.")
        return

    phone_number = contacts[name.lower()].replace("+", "")  # ✅ Remove '+'

    speak("What message should I send?")
    message = takecommand()

    if message is None:
        speak("I didn't catch that. Please try again.")
        return

    # Send message instantly and wait for WhatsApp to open
    speak(f"Sending message to {name}: {message}")
    kit.sendwhatmsg_instantly(phone_number, message, wait_time=5)

    # Wait for WhatsApp Web to load
    time.sleep(8)

    # Press 'Enter' to send the message
    pyautogui.press("enter")

    speak("Message has been sent successfully.")

# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         try:
#             audio = r.listen(source, timeout=5, phrase_time_limit=5)
#         except sr.WaitTimeoutError:
#             speak("I didn't hear anything. Please try again.")
#             return None
#
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}")
#         return query
#     except sr.UnknownValueError:
#         speak("I couldn't understand what you said. Please try again.")
#         return None
#     except sr.RequestError:
#         speak("Could not request results; check your network connection.")
#         return None
#     except Exception as e:
#         print(e)
#         speak("Say that again, please...")
#         return None
import cv2

import cv2

import cv2
import os


def capture_face(user_name):
    """Captures and saves the face of a new user."""

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cam = cv2.VideoCapture(0)

    if not os.path.exists("faces"):
        os.mkdir("faces")  # Create a folder to store faces

    user_folder = os.path.join("faces", user_name)
    if not os.path.exists(user_folder):
        os.mkdir(user_folder)

    speak(f"Look at the camera, {user_name}. Capturing images...")

    count = 0
    while count < 30:  # Capture 30 images
        ret, frame = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            count += 1
            face_img = frame[y:y + h, x:x + w]
            file_path = os.path.join(user_folder, f"{count}.jpg")
            cv2.imwrite(file_path, face_img)

        cv2.imshow("Capturing Face", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    speak(f"Face data captured for {user_name} successfully.")


import cv2
import os
import numpy as np


def train_face_recognition():
    """Trains a face recognition model using stored images."""

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    faces, labels = [], []
    label_dict = {}
    label_counter = 0

    for user_name in os.listdir("faces"):
        user_folder = os.path.join("faces", user_name)
        if not os.path.isdir(user_folder):
            continue

        label_dict[label_counter] = user_name

        for image_name in os.listdir(user_folder):
            image_path = os.path.join(user_folder, image_name)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            faces.append(image)
            labels.append(label_counter)

        label_counter += 1

    if faces:
        recognizer.train(faces, np.array(labels))
        recognizer.save("face_model.yml")  # Save trained model
        np.save("face_labels.npy", label_dict)  # Save label dictionary
        speak("Face recognition model trained successfully.")


def recognize_face():
    """Recognizes a user using the trained face recognition model."""

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("face_model.yml")  # Load trained model
    label_dict = np.load("face_labels.npy", allow_pickle=True).item()

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cam = cv2.VideoCapture(0)

    speak("Please look at the camera for verification.")

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            face_roi = gray[y:y + h, x:x + w]
            label, confidence = recognizer.predict(face_roi)

            if confidence < 50:  # Lower confidence means higher accuracy
                user_name = label_dict[label]
                speak(f"Hello, {user_name}! You are recognized.")
                cam.release()
                cv2.destroyAllWindows()
                return user_name  # Return recognized user name
            else:
                speak("Face not recognized. Access denied.")

        cv2.imshow("Recognizing Face", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    return None


# def news():
#     main_url ='https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3ff5d007fbf14110adb39dec76f254e7'
#     main_page=requests.get(main_url).json()
#     articles=main_page["articles"]
#     head=[]
#     day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
#     for ar in articles:
#         head.append(ar["title"])
#     for i in range(len(day)):
#         speak(f"today's{day[i]} news is:{head[i]}")
import requests

# import requests
#
#
# def get_news():
#     """Fetches top 5 latest news headlines."""
#
#     api_key = '3ff5d007fbf14110adb39dec76f254e7'  # Replace with your NewsAPI key
#     url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
#
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
#         news_data = response.json()
#
#         if "articles" in news_data:
#             articles = news_data["articles"][:5]  # Get top 5 news headlines
#
#             if not articles:
#                 speak("Sorry, I couldn't find any news at the moment.")
#                 return
#
#             speak("Here are the latest news headlines:")
#             for i, article in enumerate(articles, 1):
#                 title = article.get("title", "No title available")
#                 speak(f"News {i}: {title}")
#         else:
#             speak("Sorry, I couldn't fetch the news right now.")
#
#     except requests.exceptions.RequestException as e:
#         speak("There was an error fetching the news.")
#         print(f"Error: {e}")
import requests


def get_news():
    """Fetches top 5 latest news headlines from NewsAPI."""

    api_key = "3ff5d007fbf14110adb39dec76f254e7"  # Replace this with your actual NewsAPI key
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for 4xx, 5xx responses

        news_data = response.json()

        if "articles" in news_data and news_data["articles"]:
            speak("Here are the latest news headlines:")
            for i, article in enumerate(news_data["articles"][:5], 1):
                title = article.get("title", "No title available")
                print(f"News {i}: {title}")
                speak(f"News {i}: {title}")
        else:
            speak("No news articles found at the moment.")

    except requests.exceptions.ConnectionError:
        speak("I am unable to connect to the internet. Please check your connection.")
    except requests.exceptions.HTTPError as http_err:
        speak(f"HTTP error occurred: {http_err}")
    except Exception as e:
        speak("Sorry, I couldn't fetch the news at the moment.")
        print(f"Error: {e}")


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

# import threading
# import asyncio
# from scapy.all import sniff, ARP, IP, Raw
#
# global sniffer_running
# sniffer_running = True
#
#
# def packet_callback(packet):
#     """Processes and logs captured network packets."""
#     print(packet.summary())  # Show packet details in the console
#
#     # Detect Suspicious Activity
#     if packet.haslayer(ARP):
#         print("⚠️ Potential ARP Spoofing Detected!")
#         speak("Warning! ARP spoofing detected.")
#
#     elif packet.haslayer(IP) and packet.haslayer(Raw):
#         payload = packet[Raw].load.decode(errors="ignore")
#         if "password" in payload or "login" in payload:
#             print("⚠️ Possible Credential Leakage Detected!")
#             speak("Warning! Possible credential leakage detected.")
#
#
# def stop_sniffer():
#     """Stops the network sniffer."""
#     global sniffer_running
#     sniffer_running = False
#     speak("Network monitoring stopped.")
#
#
# async def async_sniff():
#     """Runs Scapy sniffer asynchronously."""
#     global sniffer_running
#     sniffer_running = True
#     print("🔍 Capturing packets... Say 'Stop network scan' to stop.")
#
#     sniff(prn=packet_callback, store=False, stop_filter=lambda _: not sniffer_running)
#
#
# def start_sniffer():
#     """Starts real-time network monitoring in a separate thread to prevent conflicts."""
#     thread = threading.Thread(target=lambda: asyncio.run(async_sniff()), daemon=True)
#     thread.start()
#     speak("Network monitoring started.")
import yfinance as yf


def get_stock_price():
    """Fetches the current stock price for a given ticker symbol."""

    speak("Which stock do you want to check?")
    stock_symbol = takecommand().upper()  # Convert input to uppercase

    try:
        stock = yf.Ticker(stock_symbol)
        stock_info = stock.history(period="1d")

        if stock_info.empty:
            speak(f"Sorry, I couldn't find stock information for {stock_symbol}. Please try again.")
            return

        current_price = stock_info["Close"].iloc[-1]  # Get last closing price
        speak(f"The current price of {stock_symbol} is {current_price} dollars.")
        print(f"📈 {stock_symbol} Current Price: ${current_price}")

    except Exception as e:
        speak("There was an error fetching the stock price.")
        print(f"Error: {e}")


import threading
from scapy.all import sniff, ARP, IP, Raw

global sniffer_running
sniffer_running = False  # Initially, sniffer is not running


def packet_callback(packet):
    """Processes and logs captured network packets."""
    print(packet.summary())  # Show packet details in the console

    # Detect Suspicious Activity
    if packet.haslayer(ARP):
        print("⚠️ Potential ARP Spoofing Detected!")
        speak("Warning! ARP spoofing detected.")

    elif packet.haslayer(IP) and packet.haslayer(Raw):
        payload = packet[Raw].load.decode(errors="ignore")
        if "password" in payload or "login" in payload:
            print("⚠️ Possible Credential Leakage Detected!")
            speak("Warning! Possible credential leakage detected.")


def sniff_packets():
    """Runs Scapy sniffer in a separate thread."""
    global sniffer_running
    sniff(prn=packet_callback, store=False, stop_filter=lambda _: not sniffer_running)


def start_sniffer():
    """Starts the network sniffer in a background thread."""
    global sniffer_running

    if sniffer_running:
        speak("Network monitoring is already running.")
        return

    speak("Starting network monitoring.")
    print("🔍 Capturing packets... Say 'Stop network scan' to stop.")

    sniffer_running = True
    sniffer_thread = threading.Thread(target=sniff_packets, daemon=True)
    sniffer_thread.start()


def stop_sniffer():
    """Stops the network sniffer."""
    global sniffer_running
    sniffer_running = False
    speak("Network monitoring stopped.")
    print("❌ Sniffer stopped.")


def open_vscode():

    try:
        path = "C:\\Users\\shiva\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)
        speak("Opening Visual Studio Code")
    except Exception as e:
        speak("Sorry, I couldn't open Visual Studio Code. Make sure it is installed in the correct directory.")

def get_weather():
    api_key = "69f23f4dc630400eb2e205149251603"  # Replace with actual API key
    city = "Bhopal"  # Replace with actual city
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url).json()
    temperature = response['current']['temp_c']
    condition = response['current']['condition']['text']
    speak(f"The temperature in {city} is {temperature} degrees Celsius with {condition}.")


import smtplib
import re


def is_valid_email(email):
    """Checks if the given email is valid."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)


def send_email():
    try:
        speak("Do you want to use voice input or type the email address?")
        mode = takecommand()

        # Get recipient email
        if "voice" in mode:
            speak("Who do you want to send the email to?")
            recipient = takecommand()
        else:
            recipient = input("Enter recipient email: ")

        if not is_valid_email(recipient):
            speak("The email address is invalid. Please try again.")
            return

        # Get subject
        speak("What is the subject?")
        subject = takecommand()
        if subject is None:
            subject = input("Enter subject: ")

        # Get message
        speak("What should I say in the email?")
        message = takecommand()
        if message is None:
            message = input("Enter message: ")

        sender_email = "Gauripandey2022@vitbhopal.ac.in"  # Replace with your email
        sender_password = input("12032004")  # More secure

        email_content = f"Subject: {subject}\n\n{message}"

        # Sending Email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, email_content)
        server.quit()

        speak("Email has been sent successfully.")

    except Exception as e:
        speak("Sorry, I couldn't send the email.")
        print(f"Error: {e}")


if __name__ == "__main__":

    wish()
    while True:
    # if 1:
        query=takecommand().lower()
        if "jarvis wake up" in query:
            print("yes sir")
            speak("yes sir")

        elif "send an email" in query:
            send_email()
        elif "exit" in query:
            speak("Goodbye!")
            sys.exit()
        elif "who are you" in query:
            print("My name is Jarvis")
            speak("My name is Jarvis")
            print(" i can do Everything that my creator programed me to do")
            speak(" i can do Everything that my creator programed me to do")
        elif "open browser" in query:
            pyautogui.hotkey('win')
            time.sleep(1)
            speak("open your brouser")
            pyautogui.typewrite('chrome',0.1)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            speak("type youtube.com",0.1)
            time.sleep(1)
            speak("press enter")
            pyautogui.press('enter')
            speak("click on the search bar")
            pyautogui.moveTo(806,125,1)

        elif ("open command prompt") in query:
            os.system("start cmd")
            #nhi chl rha
        elif "tell me about the weather" in query:
            get_weather()

        if "open vscode" in query:
             path = r"C:\Users\shiva\AppData\Local\Programs\Microsoft VS Code\bin\code"
             os.startfile(path)

        #ye nhi chl rha



        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"your IP address is{ip}")
        # elif "wikipedia" in query:
        #     speak("searching wikipedia")
        #     query=query.replace("wikipedia","")
        #     results=wikipedia.summary(query, sentences=5)
        #     speak("According to wikipedia")
        #     speak(results)
        #     print(results)
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(query, sentences=2)  # Reduced sentences for better response time
                speak(f"According to Wikipedia: {results}")
                print(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for this search. Please be more specific.")
                print(e)
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find anything on Wikipedia for that search.")
            except Exception as e:
                speak("An error occurred while searching Wikipedia.")
                print(e)

        elif " just open youtube" in query:
            webbrowser.open("www.youtube.com")
        # elif "open linkedin" in query:
        #     webbrowser.open("www.linkedin.com")
        elif "open linkedin" in query:
            speak("Do you want to open your profile or search for something?")
            choice = takecommand()

            if "my profile" in choice or "profile" in choice:
                webbrowser.open(
                    "https://www.linkedin.com/in/gauri-pandey-90a848252/")  # Replace YOUR_USERNAME with your LinkedIn profile URL
                speak("Opening your LinkedIn profile.")

            elif "search" in choice:
                speak("What do you want to search on LinkedIn?")
                search_query = takecommand()
                if search_query:
                    webbrowser.open(
                        f"https://www.linkedin.com/search/results/all/?keywords={search_query.replace(' ', '%20')}")
                    speak(f"Searching for {search_query} on LinkedIn.")

            else:
                webbrowser.open("https://www.linkedin.com")
                speak("Opening LinkedIn.")

        elif "open github" in query:
            webbrowser.open("www.github.com")
        elif "open my gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
  #search nhhi ho pa rha
        # elif "open google" in query:
        #     speak("sir,what should i search on google")
        #     qry=takecommand().lower()
        #     webbrowser.open(f"{qry}")
        #     results=wikipedia.summary(qry,sentences=1)
        #     speak(results)
        elif "open google" in query:
            speak("Sir, what should I search on Google?")
            qry = takecommand()
            if qry:
                webbrowser.open(f"https://www.google.com/search?q={qry}")
                try:
                    results = wikipedia.summary(qry, sentences=1)
                    speak(f"According to Wikipedia: {results}")
                except wikipedia.exceptions.DisambiguationError:
                    speak("There are multiple results for this search. Please be more specific.")
                except wikipedia.exceptions.PageError:
                    speak("Sorry, I couldn't find anything on Wikipedia.")
        elif "open whatsapp" in query:
            path = r"C:\Users\shiva\Downloads\WhatsApp Installer(1).exe"  # Replace with your actual path
            os.startfile(path)
            speak("Opening WhatsApp")




        elif "send massege" in query:
            kit.sendwhatmsg("+917398616219","Hello",20,41)
        elif "open youtube" in query:
            speak("what you will like to watch?")
            qrry=takecommand().lower()
            wk.playonyt(f"{qrry}")

            #error aaa rha
        elif "search on youtube" in query:
            query=query.replace("search on youtube","")
            webbrowser.open(f"www.youtube.com/result/search_query{query}")
        elif "close browser" in query:
            os.system("taskkill /f /im firefox.exe")
        elif "close chrome" in query:
            os.system("taskkill /f /im chrome.exe")
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
        elif "look the system" in query:
            os.system("rund1132.exe powrprof.d11,SetSuspendState 0,1,0")
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif "latest news" in query:
            get_news()


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

            os.startfile(os.path.join(music_dir, random.choice(songs)))
        elif "close music" in query:
            os.system("taskkill /f /im vlc.exe")
        elif "open my all desktop files" in query:
            npath= "C:\\Users\\shiva\\OneDrive\\Desktop"
            os.system(npath)
        elif "what is the time" in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strTime}")
        elif "send whatsapp message" in query:
            send_whatsapp_message()
        elif "capture my face" in query:
            speak("What is your name?")
            user_name = takecommand()
            if user_name:

                capture_face(user_name)
                train_face_recognition()

        elif "recognise my face" in query:
            recognized_user = recognize_face()
            if recognized_user:
                speak(f"Welcome back, {recognized_user}!")
            else:
                speak("Face not recognized. Please register your face first.")
        elif "scan network" in query:
            start_sniffer()
        elif "stop network scan" in query:
            stop_sniffer()
            speak("Network monitoring stopped.")
        elif "stock price" in query:
            speak("Which stock do you want to check?")
            stock_symbol = takecommand().upper()
            get_stock_price(stock_symbol)

    # elif "calculator" in query:
        #     r=sr.Recognizer()
        #     with sr.Microphone() as source:
        #         speak("ready")
        #         print("listening")
        #         r.adjust_for_ambient_noise(source)
        #         audio = r.listen(source)
        #     my_string=r.recognize_google(audio)
        #     print(my_string)
        #     def get_operator_fn(op):
        #         return {
        #             '+': operator.add,
        #             '-': operator.sub,
        #             '*': operator.mul,
        #             'divided':operator.__truediv__,

                #
                # }[op]





        # pi.press('win')
        # time.sleep(1)
        # pi.typewrite('notepad',1)
        # pi.press("enter")
        # time.sleep(2)
        # pi.typewrite('how to manual')







        speak("sir,do you have any other work")
#
#
