import speech_recognition as sr
import os
import win32com.client
import webbrowser
import openai
import datetime
import random

from openai import OpenAI
from config import OPENAI_API_KEY

chatStr = ""

def chat(query):
    global chatStr
    #remove this below print statement if required to stop printing reply from jarvis
    print(chatStr)
    client = OpenAI(api_key=OPENAI_API_KEY)

    chatStr += f"Liku: {query}\n Jarvis: "
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": chatStr
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap this inside a try catch block

    speaker.Speak(response.choices[0].message.content)
    chatStr += f"{response.choices[0].message.content}\n"
    return response.choices[0].message.content


    # with open(f"Openaisolutions/prompt- {random.randint(1, 1000099)}", "w") as f:
    with open(f"Openaisolutions/{prompt[0:30]}", "w") as f:
        f.write(text)


def ai(prompt):
    client = OpenAI(api_key=OPENAI_API_KEY)
    text = f"OpenAI response for Prompt:{prompt} \n************************\n \n"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    #todo: wrap this inside a try catch block

    print(response.choices[0].message.content)
    text += response.choices[0].message.content
    if not os.path.exists("Openaisolutions"):
        os.mkdir("Openaisolutions")

    #with open(f"Openaisolutions/prompt- {random.randint(1, 1000099)}", "w") as f:
    with open(f"Openaisolutions/{prompt[0:30] }", "w") as f:
        f.write(text)


speaker = win32com.client.Dispatch("SAPI.SpVoice")

"""while 1:
    print("Enter the word to be spoken:")
    s = input()
    speaker.Speak(s)"""


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =  0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="En-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"



if __name__ == '__main__':
    print('PyCharm')
    speaker.Speak("Hello I am Jarvis A I ")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])



        if "open music" in query:
            musicPath = "D:/Tumse.mp3"
            os.system(f"start {musicPath}")

        elif "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speaker.Speak(f"sir! the time is {strfTime}")
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speaker.Speak(f"Jo ki hai {hour} baajkeai {min} minutes")

        elif "open mongoDB".lower() in query.lower():
            os.system(f"start C:/Users/HP/AppData/Local/MongoDBCompass/MongoDBCompass.exe")

        elif "open postman".lower() in query.lower():
            os.system(f"start C:/Users/HP/AppData/Local/Postman/Postman.exe")

        elif "Artificial Intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            charStr = ""

        else:
            print("chatting...")
            chat(query)


#todo:weather api, news api,




        #speaker.Speak(query)




