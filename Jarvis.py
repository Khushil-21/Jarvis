"""
1. able to speak: text to speech (tts) - gtts, pyttsx3
2. understand: speech recognition (voice to text)

Tell a joke                   ✅
tell todays date              ✅
tell todays time              ✅
Take a screen shot            ✅
Open an app                   ✅
Open a website                ✅
Current Location              ✅
Set alarm                     ✅
Search on wikipedia           ✅
Send Whatsapp msg to someone  ✅

"

5am to 12pm: Good Morning
12pm to 5pm: Good Afternoon
5pm to 12am: Good Evening
12am to 5am: Its very late , You should go to sleep
"

"""
""" ---------------------------------- IMPORTING MODULES---------------------------------------"""
import pyttsx3
import speech_recognition as sr
from AppOpener import open
import pyaudio
from random import choice
import webbrowser
from datetime import *
import os
import geocoder
import wikipedia
import pywhatkit
import pyautogui
import geocoder
# import google
from PIL import ImageGrab ,Image
import playsound
import time
import winsound


""" ---------------------- STARTING ENGINE FOR Speech Recognisation ----------------------------"""
engine = pyttsx3.init()
engine.setProperty("rate",220)
# rate = engine.getProperty('rate')
# print(rate)
voices = engine.getProperty("voices")
# print(voices)
engine.setProperty("voice", voices[1].id)

""" ------------------------- IMPORTANT FUNCTIONS & VARIBLES -------------------------------"""

jokes = [                               #! list of jokes
    """Why did an old man fall in a well?Because he couldn't see that well!""",
    
    """Why did the actor fall through the floorboards?They were going through a stage!""",
    
    """Why did a scarecrow win a Nobel prize?He was outstanding in his field!""",
    
    """Why are peppers the best at archery?Because they habanero!""",
    
    """What did the duck say after she bought chapstick?Put it on my bill!""",
    
    """What do you call a fake noodle?An impasta!""",
    
    """What did the three-legged dog say when he walked into a saloon?“I'm looking for the man who shot my paw!”""",
    
    """How do you tell the difference between a bull and a cow?It is either one or the udder!""",
    
    """What's red and smells like blue paint?Red paint!""",
    
    """What's the difference between a hippo and a Zippo?One is very heavy, the other is a little lighter!""",
]

how_m_i=[                               #! list of answer
        """I m fine """,
        """I m good """,
        """I m doing great today """,
        """I m very happy  """

]

def talk(text):                         #! for talking
    # text=text.split()
    # print()
    # for word in text:
    #     print(word,end=' ')
    #     engine.say(word)
    #     engine.runAndWait()
    #     # t.sleep(3)
    text=str(text)
    print(text)
    text=text.replace('*','Multiply by')
    text=text.replace('/','divide by')
    text=text.replace('khushil','khuushil')
    # print(text)
    engine.say(text)
    engine.runAndWait()

def welcome():                          #! for greeting someone 
    date = datetime.today()
    # date=time(17,30,3,3)
    if date.hour < 12:
        talk("Good morning khushil!! How can i help you ?? ")
    elif date.hour<16.30:
        talk("Good afternoon khushil!! How can i help you ?? ")
    elif date.hour<21:
        talk("Good evening khushil!! How can i help you ?? ")
    else:
        talk("Go to sleep khushil!! How can i help you ?? ")

def listen():                           #! for identifying voice 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        talk("\nListening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        talk("\nI think you said:- " + text)

    except sr.UnknownValueError:
        talk("\nSorry, I can't understand what you just said. Could you speak that again?")
        text = ""

    except sr.RequestError as e:
        talk("Could not request results from Google Speech Recognition service; {0}".format(e))
        text = ""

    return text

def current_detail(acess):              #! gives current date amd time 
    dt = datetime.today()
    if acess==1:
        talk(dt.strftime("%m/%d/%Y"))
    elif acess==2:
        talk(dt.strftime("%I:%M:%S"))
    elif acess==3:
        talk(dt.strftime("%m/%d/%Y, %I:%M:%S"))
    return 'time given'

def current_location():                 #! Gives Current Locaton through google maps
    g = geocoder.ip('me')
    lat=str(g.latlng[0])
    lng=str(g.latlng[1])
    s="https://www.google.com/maps/@"+lat+lng+"18z"
    webbrowser.open(s)

def take_written_input(message):        #! Takes written input from user 
    talk(message)
    return input("Type your answer here ----> ").lower()

def change_input():
    global input_type
    global selected_input
    if input_type=='voice' and selected_input=='written':
        talk("\n--------------------- Voice Input Is Deactivated & Written Input Is Activated ------------------------\n")
        input_type='written'
    elif input_type=='written' and selected_input=='voice':
        talk("\n--------------------- Voice Input Is Activated & Written Input Is Deactivated ------------------------\n")
        input_type='voice'
    # input_type='written'

def set_alarm():
    n=take_written_input("Enter time to set alarm format[hh:mm:ss] :- ")
    alarmTime = n.split(":")
    HOUR = datetime.now().hour
    min = datetime.now().minute
    rem_hr=abs(int(alarmTime[0])-HOUR)
    rem_min=abs(int(alarmTime[1])-min)
    rem_sec=(rem_hr*60*60)+(rem_min*60)
    for i in reversed(range(rem_sec)):
        talk(str(i))
    playsound.playsound("K:\\Study\\My Unquie Projects\\JARVIS\\sound.mp3")


""" ---------------------------------- MAIN CODE ---------------------------------------"""
welcome()
count=0
input_type='voice'
selected_input=''
while True:
    if input_type!=selected_input and selected_input!='':
        change_input()
    if selected_input=='':
        talk("\n--------------------- Voice Input is Activated ---------------------\n")
        selected_input='voice'
    if input_type=='voice':
        query = listen()
    if input_type=='written':
        query=take_written_input("How Can i help you ?")
    query=query.lower()
    if "bye" in query or "see you" in query:
        talk("Good bye Khushil")
        break

    if "joke" in query or "make me laugh" in query:
        joke = choice(jokes)
        joke=joke.split('?')
        talk(joke[0])
        talk(joke[1])
    
    if "." in query:  #! please open google.com
        for string in query.split():
            if "." in string:
                url = string
        if "www." not in url:
            url = "www." + url
        webbrowser.open(url)

    if "current date" in query or "current time" in query or "today's date" in query or "today's time" in query or "what is time " in query or "time right now" in query:
        if "date" in query and "time" not in query:
            acess=1
        elif "date" not in query and "time" in query:
            acess=2
        else:
            acess=3
        current_detail(acess)

    if "how are you" in query:
        text = choice(how_m_i)
        talk(text)
        talk("You are very kind to ask 🥰") 
    
    if "how old are you" in query or "how old you are" in query or "your age" in query or "were you created" in query or "your birth date" in query:
        talk("So basically i was initially created on 21st May 2022")
        talk("But still some more advanced features are being updated in me regularly")

    if "where m i" in query or "current location" in query or "current lattitude and longitude" in query or "my location" in query:
        current_location()

    if "wikipedia" in query:
        if "about" in query:
            query=query.split('about')
        else:
            query=list(query.split('`'))
        for target in query:
            if "from wikipedia" in target:
                target=target.replace("from wikipedia","")
                target=wikipedia.summary(target, sentences='3')
                talk(target)

    if "screenshot" in query or "on my screen" in query:
        ss_img = ImageGrab.grab()
        count+=1
        ss_img.save(f'K:\\Study\\My Unquie Projects\\JARVIS\\ss{count}.png','PNG')
        ss_img.show()                
    
    if "whatsapp" in query:
        talk("\n--------------- Temporerily Written input is Activated For your convinience --------------\n")
        talk("What is the message ? ")
        msg=take_written_input("Enter your message in space give below ")
        talk("to whom ?")
        phn=take_written_input("Enter Reciver's phone number in space give below ")
        pywhatkit.sendwhatmsg_instantly(f"+91{phn}",msg)

    if "open" in query:
        i=query[5:]
        print("OPENING",i)
        open(i)

    if "alarm" in query:
        set_alarm()

    if '+' in query or '-' in query or 'x' in query or '/' in query or 'into' in query:
        query=query.replace('x','*')
        query=query.replace('into','*')
        talk(f"{query} = {eval(query)}")

    

    if query!='':
        talk("What next ?")
    else:
        c=0
        if input_type=='voice':
            while True:
                talk("Do you want to Activate Written input ( yes or no )")
                choice=listen().lower()
                if choice=='':
                    c+=1
                    if c>=2:
                        talk("\n--------------- Due to in some error in voice input Temporerily Written input is activated --------------\n")
                        choice=take_written_input("Do you want to Activate Written input ( yes or no )")
                        if choice=='yes':
                            selected_input='written'
                        if choice=='no':
                            selected_input='voice'
                        break
                if choice=='yes':
                    selected_input='written'
                    break
                if choice=='no':
                    selected_input='voice'
                    break
                
                if choice!='yes' and choice!='no' and choice!='':
                    talk("Please answer in yes or no only")
                    continue

    if input_type=='written':
        if query=='':
            talk("Please type something i can not process empty String\nType Again ")
            continue
        while True:
                choice=take_written_input("Do you want to Activate Voice input ( yes or no )")
                if choice!='yes' and choice!='no':
                    talk("Please type answer yes or no only")
                    continue
                if choice=='no':
                    selected_input='written'
                    break
                if choice=='yes':
                    selected_input='voice'
                    break