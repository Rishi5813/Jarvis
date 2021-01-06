# This is the File which contains all the Questions and Replies of Jarvis 
# This is the Male voiced Jarvis.
# This Project is made and maintained by Rishi Jani. Each and every line Of the code is Written 
# By Rishi Jani.

# Jarvis is a A.I. for All Cross Platforms.
# No-One Can use This Code for Harmful Purposes.

# Since this is a Python Program we need all the Project Dependencies and the Modules, it is optional as I can compile this program to and .exe and give it to Github. But anyone building this Program with pyinstaller on his or her computer will need all the dependencies.

# pip install :-
# pyautogui
# subprocess
# webbrowser
# wikipedia
# bluetooth
# Speech Recognition
# win10toast
# PIL
# playsound
# googlesearch
# pydictionary
# selinium


# All The Imports:-

import datetime
import os
import sys
import subprocess
import pyautogui
import webbrowser
import pyttsx3
import bluetooth
import speech_recognition as sr
import wikipedia
import pytesseract
import time
from tkcalendar import *
from tkinter import *
from win10toast import ToastNotifier
from PIL import Image
from selenium import webdriver
from PyDictionary import PyDictionary
from googlesearch import search
from playsound import playsound

# Defining The functions
dictionary = PyDictionary()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 193)

# speak() Function Defined
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# wake() Functon to Wake up the Program when the User says a Particular WAKE_WORD Which in this Program is "Jarvis".
def wake():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        r.pause_threshold = 2
        r.dynamic_energy_threshold = True
        audio = r.listen(source)

    try:
        wake_word = r.recognize_google(audio, language='en')

    except Exception as e:
        pass
        return "None"
    return wake_word
# Giving Options in the program.
def options():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        r.pause_threshold = 2
        r.dynamic_energy_threshold = True
        audio = r.listen(source)

    try:
        option_answer= r.recognize_google(audio, language='en')

    except Exception as e:
        pass
        return "None"
    return option_answer

# take_command() function to Take voice Command as a input and execute the command based on the conditional statements, Which start from the line 111 and can be extended as much as possible to make Jarvis Intelligent.
def take_command():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en')
        print("You Said -", query)

    except Exception as e:
        print("I Couldn't Understand, Please Repeat")
        speak("i couldn't understand, Please Repeat")
        return "None"
    return query
    
def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())

while True:
    wake_word: str = wake().lower()
    if 'jarvis' in wake_word or '' in wake_word:
        if __name__ == '__main__':
            while True:
                query: str = take_command().lower()

                # General Commands (Casual or Time-Pass)

                if 'what can you do' in query:
                    print("     _____                       ")
                    print("    /     \  - Anything for you! ")
                    print("   |  * *  |                     ")
                    print("    \_---_/                      ")
                    print("      | |                        ")
                    speak("I am your personal assistant , i can do anything for you ")
                    speak("These are Some Things you can Command Me:")
                    print("These are Some Things you can Command Me:")
                    print("Wikipedia - for Descriptions of People and Other Things")
                    print("Open + Name of the App / Website - for Opening Apps and Websites")
                    print("Where Is + Name of the Place - For Finding Location of Places")
                    print("What Is + The Word You Want to Search - To Search on Web")
                    print(
                        "What Is The Definition/Synonym/Antonym Of + The Word - To Find The "
                        "Definition/Antonym/Synonym Of "
                        "any Word")
                    print("Pause - To Stop Me Temporarily")
                    print("Close - To Exit me")
                    run("python Jarvis-1st.py")
                elif 'sweet dreams' in query or 'good night' in query:
                    hour = int(datetime.datetime.now().hour)
                    if 0 <= hour < 7:
                        speak('okay, Good night, bye')
                        sys.exit()
                    elif 7 <= hour < 16:
                        speak("well, it isn't the time of sleeping, now")
                    else:
                        speak("well, it isn't the time of sleeping, now")
                elif 'good morning' in query or 'good night' in query:
                    hour = int(datetime.datetime.now().hour)
                    if 0 <= hour < 11:
                        speak('good morning')
                    elif 12 <= hour < 20:
                        speak("well, it isn't morning now ")
                    else:
                        speak("well, it isn't morning, now")
                elif "tell me some jokes" in query:
                    import pyjokes
                    joke = pyjoke.get_joke()
                    speak("okay, here's something that will make you laugh")
                    print(joke)
                    speak(joke)
               
                elif 'who are you' in query:
                    speak("Firstly I am your personal assistant, secondly i was first made by Rishi and thirdly you can call me Jarvis")   
    
                elif 'what is your name' in query:
                    print("     _____                       ")
                    print("    /     \ - I Am your Personal Assistant, you can call me Jarvis ")
                    print("   |  * *  |                     ")
                    print("    \_---_/                      ")
                    print("      | |                        ")
                    speak("i am your personal assistant, you can call me Jarvis, and it's not hard to speak !,ha ha")
                    run("python Jarvis-1st.py")
                elif 'talk to me in' in query:
                    print("     _____                       ")
                    print("    /     \ - Sorry, but i am not multillingual ")
                    print("   |  * *  |                     ")
                    print("    \_---_/                      ")
                    print("      | |                        ")
                    speak("sorry, but i cannot talk in different languages")
                    run("python Jarvis-1st.py")
                elif 'how do you do' in query:
                    print("     _____                       ")
                    print("    /     \ - Well, I Am Fine   ")
                    print("   |  * *  |                     ")
                    print("    \_---_/                      ")
                    print("      | |                        ")
                    speak("well i am fine, how about you !")
                    run("python Jarvis-1st.py")
                elif 'sing me a song' in query:
                    print("aaaaaa..... 😅")
                    speak("I would rather not sing, i am very bad at singing")
                elif 'sing a song' in query:
                    print("aaaaaa..... 😅")
                    speak("I would rather not sing, i am very bad at singing")
                elif 'sing song' in query:
                    print("aaaaaa..... 😅")
                    speak("I would rather not sing, i am very bad at singing")
                elif 'sing us a song' in query:
                    print("aaaaaa..... 😅")
                    speak("I would rather not sing, i am very bad at singing")
                elif 'where are you' in query:
                    print("I live in your Device and I am always Ready to Help you 😄")
                    speak("I live in your Device and I am always Ready to Help you")
                elif "why can't you do anything" in query:
                    print("I am really sorry for my mistake 😔, Please forgive me")
                    speak("I am really sorry for my mistake, Please forgive me")
                elif "how can you be so careless" in query:
                    print("I am really sorry for my mistake 😔, Please forgive me")
                    speak("I am really sorry for my mistake, Please forgive me")
                
                    
                # General Commands (Useful)

                elif 'call' in query:
                    speak("sorry, but i may not be able to do that at the moment, but you can call by using google duo")
                    command = "C:/Program Files (x86)/Microsoft Office/root/Office16/MSACCESS.EXE"
                    subprocess.Popen(command)
                    subprocess.Popen(command)
                    speak("Please try and find the person you want to call")
                    run("python Jarvis-1st.py")
                elif 'play music' in query:
                    print("Sorry, but I Cannot do that at the Moment")
                    speak("sorry, i may not be able to do that at the moment, but you can enjoy the music by the "
                          "spotify app")
                    run("python Jarvis-1st.py")
                elif 'wikipedia' in query:
                    print("Searching")
                    speak('Searching in Wikipedia...., please wait')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=3)
                    print(results)
                    speak("According to Wikipedia")
                    speak(results)
                    run("python Jarvis-1st.py")
                elif 'take a screenshot' in query:
                    speak("Taking")
                    image = pyautogui.screenshot()
                    speak("please enter the name of the screenshot you want to save")
                    image_name = input('Name of the shot:-')
                    path = "E:/Screenshots by Jarvis/" + image_name + ".png"
                    image.save(path)
                    speak("screenshot taken, check your screenshot folder")
                    run("python Jarvis-1st.py")
                elif 'where is' in query:
                    playsound("E:/on.mp3")
                    print("Please Wait, I will Show you")
                    speak('please wait, i can show you the place')
                    place = query = query.replace("where is", "")
                    url = "https://www.google.com/maps/place/" + str(place)
                    webbrowser.open(url)
                    results = wikipedia.summary(place, sentences=3)
                    speak(results)
                    run("python Jarvis-1st.py")
                elif 'what are you doing' in query:
                    print("     _____                       ")
                        print("    /     \  - Helping You!      ")
                    print("   |  * *  |                     ")
                    print("    \_---_/                      ")
                    print("      | |                        ")
                    speak("Just helping you, and my team is making me better and better eveyday at this task")
                    run("python Jarvis-1st.py")
                elif "show the calendar" in query:
                    root = Tk()
                    root.title('Calender')
                    root.geometry("600x400")
                    cal = Calendar(root, selectmode = "day", year = 2020, month =11, day =14)
                    cal.pack()
                    mylabel = Label(root, text="")
                    mylabel.pack()
                    def grab_date():
                        mylabel.config(text = "Today's date is" + cal.get_date())
                    mybutton = Button(root, text ="Select Date", command = grab_date())
                    mybutton.pack()
                    root.mainloop()
                    run("python Jarvis-1st.py")
                elif "what's today's date" in query:
                    Current_Date = datetime.datetime.today()
                    speaking = 'Today is', Current_Date
                    print(speaking)
                    speak(speaking)
                    run("python Jarvis-1st.py")
                elif 'what is the time' in query:
                    starTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak("sir, the time is")
                    print(starTime)
                    speak(starTime)
                    run("python Jarvis-1st.py")
                elif 'what is the definition of' in query:
                    print("Got It")
                    speak("finding, Please wait")
                    define = query = query.replace("what is the definition of", "")
                    print(dictionary.meaning(define, ))
                    speak(dictionary.meaning(define))
                    run("python Jarvis-1st.py")
                elif 'what is the synonym of' in query:
                    print("Got It")
                    speak("finding, Please wait")
                    word = query = query.replace("what is the synonym of", "")
                    print(dictionary.synonym(word, ))
                    speak(dictionary.synonym(word))
                    run("python Jarvis-1st.py")
                elif 'what is the antonym of' in query:
                    print("Got It")
                    speak("finding, Please wait")
                    word = query = query.replace("what is the antonym of", "")
                    print(dictionary.antonym(word, ))
                    speak(dictionary.antonym(word))
                    run("python Jarvis-1st.py")
                elif 'what is ' in query:
                    print("Opening")
                    speak("Please wait, i will search for you")
                    query = query.replace("what is", "")
                    results = wikipedia.summary(query, sentences=3)
                    speak("According to Wikipedia")
                    speak(results)
                    speak("here are some links, please check them")
                    query = query.replace("what is", "")
                    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                        print(j)
                    query = query.replace(' ', '+')
                    browser = webdriver.Chrome('chromedriver')
                    for i in range(1):
                        matched_elements = browser.get("https://www.google.com/search?q=" +
                                                       query + "&start=" + str(i))
                    run("python Jarvis-1st.py")
                elif 'browse the web for' in query:
                    print("Opening")
                    speak("Please wait, i will search for you")
                    query = query.replace("browse the web for", "")
                    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                        print(j)
                    query = query.replace(' ', '+')
                    browser = webdriver.Chrome('chromedriver')
                    for i in range(1):
                        matched_elements = browser.get("https://www.google.com/search?q=" +
                                                       query + "&start=" + str(i))
                    run("python Jarvis-1st.py")
                elif 'search the web for' in query:
                    print("Opening")
                    speak("Please wait, i will search for you")
                    query = query.replace("search the web for", "")
                    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                        print(j)
                    query = query.replace(' ', '+')
                    browser = webdriver.Chrome('chromedriver')
                    for i in range(1):
                        matched_elements = browser.get("https://www.google.com/search?q=" +
                                                       query + "&start=" + str(i))
                    run("python Jarvis-1st.py")
                elif 'why is ' in query:
                    print("Opening")
                    speak("Please wait, i will give you some helpful links")
                    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                        print(j)
                    query = query.replace(' ', '+')
                    browser = webdriver.Chrome('chromedriver')
                    for i in range(1):
                        matched_elements = browser.get("https://www.google.com/search?q=" +
                                                       query + "&start=" + str(i))
                    run("python Jarvis-1st.py")

                # Opening Websites

                elif 'open youtube' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    webbrowser.open("https://www.youtube.com/")
                    run("python Jarvis-1st.py")
                elif 'open edu sprint' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    webbrowser.open("http://thakur.edusprint.in/thakur/Portal/Default/IndexLite?_ca=1943187191")
                    run("python Jarvis-1st.py")
                elif 'open stack overflow' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    webbrowser.open("https://stackoverflow.com/")
                    run("python Jarvis-1st.py")
                elif 'open hot-star' in query:
                    print("Opening....")
                    speak("Opening")
                    webbrowser.open("https://www.hotstar.com/in")
                    run("python Jarvis-1st.py")
                elif 'open my coding website' in query:
                    print("Opening....")
                    speak("Opening")
                    webbrowser.open("https://repl.it/")
                    run("python Jarvis-1st.py")
                elif 'open python website' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    webbrowser.open("https://www.python.org/")
                    run("python Jarvis-1st.py")
                elif 'open google drive' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    webbrowser.open("https://drive.google.com/drive/u/0/my-drive")
                    run("python Jarvis-1st.py")
                elif 'open google slides' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    webbrowser.open("https://docs.google.com/presentation/u/0/")
                    run("python Jarvis-1st.py")
                elif 'open google docs' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    webbrowser.open("https://docs.google.com/document/u/0/")
                    run("python Jarvis-1st.py")
                elif 'open google sheets' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    webbrowser.open("https://docs.google.com/spreadsheets/u/0/")
                    run("python Jarvis-1st.py")
                elif 'open google earth' in query:
                    print("Opening")
                    speak("Opening, Please wait")
                    webbrowser.open("https://earth.google.com/web/?authuser=0")
                    run("python Jarvis-1st.py")
                elif 'open google play ' in query:
                    print("Opening")
                    speak("Opening, Please wait")
                    webbrowser.open("https://play.google.com/?hl=en&authuser=0")
                    run("python Jarvis-1st.py")
                elif 'open g mail' in query:
                    print("Opening")
                    speak("Opening, Please wait")
                    webbrowser.open("https://mail.google.com/mail/?authuser=0")
                    run("python Jarvis-1st.py")
                elif 'open google scholar' in query:
                    print("Opening....")
                    speak("Opening")
                    webbrowser.open("https://scholar.google.com/")
                    run("python Jarvis-1st.py")
                elif 'open google maps' in query:
                    print("Opening")
                    speak("Opening, Please wait")
                    webbrowser.open("https://maps.google.co.in/maps?hl=en&tab=rl&authuser=0")
                    run("python Jarvis-1st.py")
                elif 'open google news' in query:
                    print("Opening")
                    speak("Opening, Please wait")
                    webbrowser.open("https://news.google.com/?tab=rn&authuser=0")
                    run("python Jarvis-1st.py")
                elif 'open google duo' in query:
                    print("Opening")
                    speak("Opening, Please wait")
                    webbrowser.open("https://duo.google.com/?usp=duo_ald")
                    run("python Jarvis-1st.py")
                elif 'open google' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    webbrowser.open("https://www.google.com/")
                    run("python Jarvis-1st.py")

                # Opening Apps

                elif 'open virtualbox' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    command = "C:/Program Files/Oracle/VirtualBox/VirtualBox.exe"
                    subprocess.Popen(command)
                    run("python Jarvis-1st.py")
                elif 'open powerpoint' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    command = "C:/Program Files (x86)/Microsoft Office/root/Office16/POWERPNT.EXE"
                    subprocess.Popen(command)
                    run("python Jarvis-1st.py")
                elif 'open excel' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    command = "C:/Program Files (x86)/Microsoft Office/root/Office16/EXCEL.EXE"
                    subprocess.Popen(command)
                    run("python Jarvis-1st.py")
                elif 'open word' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    command = "C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE"
                    subprocess.Popen(command)
                    run("python Jarvis-1st.py")
                elif 'open acces' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    command = "C:/Program Files (x86)/Microsoft Office/root/Office16/MSACCESS.EXE"
                    subprocess.Popen(command)
                    run("python Jarvis-1st.py")
                elif 'open outlook ' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    command = "C:/Program Files (x86)/Microsoft Office/root/Office16/OUTLOOK.EXE"
                    subprocess.Popen(command)
                    run("python Jarvis-1st.py")
                elif 'open webex' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    command = "C:/Program Files (x86)/Webex/Webex/Applications/ptoneclk.exe"
                    subprocess.Popen(command)
                    run("python Jarvis-1st.py")
                elif 'open zoom' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    command = "C:/Users/rishi/AppData/Roaming/Zoom/bin/Zoom.exe"
                    subprocess.Popen(command)
                    run("python Jarvis-1st.py")
                elif 'open intelli j idea' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    command = "C:/Program Files/JetBrains/IntelliJ IDEA Community Edition 2020.2/bin/idea64.exe"
                    subprocess.Popen(command)
                    run("python Jarvis-1st.py")
                elif 'open telegram' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    command = "A:/Telegram Desktop/Telegram.exe"
                    subprocess.Popen(command)
                    run("python Jarvis-1st.py")
                elif 'open whatsapp' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    command = "C:/Users/rishi/AppData/Local/WhatsApp/WhatsApp.exe"
                    subprocess.Popen(command)
                    run("python Jarvis-1st.py")
                elif 'open microsoft edge ' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    command = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
                    subprocess.Popen(command)
                    run("python Jarvis-1st.py")
                elif 'open mac fee' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    command = "C:/Program Files/Common Files/McAfee/Platform/McUICnt.exe"
                    subprocess.Popen(command)
                    run("python Jarvis-1st.py")
                elif 'open vs code' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    command = "C:/Users/rishi/AppData/Local/Programs/Microsoft VS Code/Code.exe"
                    subprocess.Popen(command)
                    run("python Jarvis-1st.py")
                elif 'open apple mail' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    command = "C:/Program Files (x86)/Common Files/Apple/Internet Services/iCloudWeb.exe mail"
                    subprocess.Popen(command)
                    run("python Jarvis-1st.py")
                elif 'open turbo c ' in query:
                    print("Opening....")
                    speak("Opening, Please wait")
                    command = "C:/TURBOC3/Turbo C++/"
                    subprocess.Popen(command)
                    run("python Jarvis-1st.py")

                # System Commands and Jarvis main commands

                elif 'disable Wi-Fi' in query:
                    run("netsh interface set interface 'Wifi' disabled")
                    speak("wi-fi disabled")
                    run("python Jarvis-1st.py")
                elif 'read the screen' in query:
                    image = pyautogui.screenshot()
                    path = "E:/Screenshots by Jarvis/screen.png"
                    image.save(path)
                    image2 = Image.open('E:/Screenshots by Jarvis/screen.png')
                    text = pytesseract.image_to_string(image2)
                    print(text)
                    speak(text)
                    run("python Jarvis_with_wake.py")
                    run("python Jarvis-1st.py")

                elif 'enable wi-fi' in query:
                    run("netsh interface set interface 'Wifi' enabled")
                    speak("wi-fi enabled")
                    run("python Jarvis_with_wake.py")
                    run("python Jarvis-1st.py")
                elif 'bluetooth devices' in query:
                    nearby_devices = bluetooth.discover_devices(lookup_names=True)

                    print("found %d devices" % len(nearby_devices))

                    for name, addr in nearby_devices:
                        print(" %s - %s" % (addr, name))
                    run("python Jarvis-1st.py")
                elif "change your voice to male" in query or "change your voice" in query:
                    speak("okay, i am changing, just a second")
                    run("python c:/users/rishi/Pycharm Projects/Jarvis/Jarvis-Male Voice/Jarvis_Main.py")
                elif 'exit' in query:
                    print("     _____            ")
                    print("    /     \   -> Bye !")
                    print("   |  * *  |          ")
                    print("    \_---_/           ")
                    print("      | |             ")
                    speak("I am closing myself, please restart me to speak to me again")
                    playsound("off.mp3")
                    sys.exit()
                elif 'close' in query:
                    print("     _____            ")
                    print("    /     \   -> Bye !")
                    print("   |  * *  |          ")
                    print("    \_---_/           ")
                    print("      | |             ")
                    speak("I am closing , nice talking with you")
                    playsound("off.mp3")
                    sys.exit()
                elif 'bye' in query:
                    print("     _____            ")
                    print("    /     \  -> Bye !")
                    print("   |  * *  |          ")
                    print("    \_---_/           ")
                    print("      | |             ")
                    speak("bye , take care")
                    playsound("off.mp3")
                    sys.exit()
                elif 'stop' in query:
                    print("Stopped")
                    speak("I am Paused, press any key to speak to me again")
                    playsound("jarvis_beep.mp3")
                    run("python Jarvis_with_wake.py")
                elif 'pause' in query:
                    print("Stopped")
                    speak("I am Paused, press any key to speak to me again")
                    playsound("jarvis_beep.mp3")
                    run("python Jarvis_with_wake.py")
                elif 'hey jarvis' in query:
                    print("     _____                    ")
                    print("    /     \  -> Here for Help!")
                    print("   |  * *  |                  ")
                    print("    \_---_/                   ")
                    print("      | |                     ")
                    speak("here i am!)
                elif 'are you there' in query:
                    print("     _____                    ")
                    print("    /     \   -> Here for you!")
                    print("   |  * *  |                  ")
                    print("    \_---_/                   ")
                    print("      | |                     ")
                    speak("at your service sir")
                elif 'hello' in query:
                    print("Hi")
                    speak("hai")
                elif 'hai' in query:
                    print("Hello")
                    speak("Hello")
                elif 'hi' in query:
                    print("Hello")
                    speak("Hello")
                elif "  " in query:
                    print("That Might Be Beyong My Abilities for Now.")
                    speak("That might be beyond my abilities for now")
                    run("python Jarvis_with_wake.py")