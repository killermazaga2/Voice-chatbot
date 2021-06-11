from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import pyttsx3
import speech_recognition as sr
import threading

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(talk):
    engine.say(talk)
    engine.runAndWait()
talk("Welcome user")
bot = ChatBot("alexa")

greetings=[
    'Hello',
    'hi there!',
    'Hello',
    'Hello there',
    'Hi',
    'Hi there',
    'Hi',
    'Hello there',
    'Good morning',
    'Good morning to you too',
    'Good evening',
    'Good evening to you too',
]

information=[
    'What is your name?',
    'My name is Alexa',
    'Who developed you?',
    'I was developed by Tinesh',
    'Who is your owner?',
    'My owner is Tinesh',
    'Who is your friend?'
    'My friend is Tinesh',
    'Where are you from',
    "I'm from Tinesh's heart",
    'Where are you from?',
    "I'm from Chennai",
    "Where are you from?",
    "I'm from Chennai too",
    "What is your owner doing?",
    'My owner is exploring his life'
]

ending=[
    'Okay, bye bye',
    'Bye bye',
    'Bye bye to you too',
    'Yes, bye',
    'Good night',
    'Good night to you too',
    'Take care',
    'Yes, you too',
    'You too take care',
    'Peace out',
    'Peace out bro',
    'Ta ta',
    'Ta ta bye bye',
    "I'm going to sleep",
    "Go to sleep, then",
    "I want to sleep",
    "Okay good night then"
]

trainer = ListTrainer(bot)

# #Train with trainers

trainer.train(greetings)
trainer.train(information)
trainer.train(ending)


# print('Tak to alexa')
# while True:
#     query=input()
#     if query=='exit':
#         break
#     answer= bot.get_response(query)
#     print("alexa: ", answer)

main=Tk()

main.geometry("500x650")

main.title("Alexa the ChatBot")

def take_query():
    listener = sr.Recognizer()
    listener.pause_threshold=1
    with sr.Microphone() as source:
        print("Alexa is listening ...")
        try:
            voice = listener.listen(source)
            query = listener.recognize_google(voice, language='eng-in')
            query = query.lower()
            print(query)
            textF.delete(0, END)
            textF.insert(0, query) 
            if 'time' in query:
                time = datetime.datetime.now().strftime('%H:%M %p')
                msgs.insert(END, "You: "+ query)
                msgs.insert(END, "alexa: The current time is  "+ time)
                talk('The current time is: '+ time)
                textF.delete(0,END)
                msgs.yview(END)
            elif 'play' in query:
                song = query.replace('play', '')
                pywhatkit.playonyt(song)
                msgs.insert(END, "You: "+ query)
                msgs.insert(END, "alexa: Playing  "+ song)
                talk('Playing'+ song)
                textF.delete(0,END)
                msgs.yview(END)
            elif 'wikipedia' in query:
                person= query.replace('wikipedia','')
                info= wikipedia.summary(person, 1)
                msgs.insert(END, "You: "+ query)
                msgs.insert(END, "alexa: "+ info)
                talk(info)
                textF.delete(0,END)
                msgs.yview(END)
            elif 'joke' in query:
                py_joke =pyjokes.get_joke 
                msgs.insert(END, "You: "+ query)
                msgs.insert(END, "alexa: "+ py_joke)
                talk(py_joke)
            elif 'search' in query:
                search= query.replace('search', '')
                url= 'https://google.com/search?q=' + search
                webbrowser.get().open(url)
                msgs.insert(END, "You: "+ query)
                msgs.insert(END, "alexa: Here is what I have found "+ search)
                talk("Here is what I have found")
            elif 'instagram' in query:
                url='https://www.instagram.com/'
                webbrowser.get().open(url)
                msgs.insert(END, "You: "+ query)
                msgs.insert(END, "alexa: Happy Insta gramming")
                talk("Happy Instagramming")
            else:
                ask_from_alexa()    
        except Exception as e:
            print(e)
            print("Not recognized")
def ask_from_alexa():
    query = textF.get()
    answer_from_bot= bot.get_response(query)
    msgs.insert(END, "You: "+ query)
    msgs.insert(END, "alexa: "+ str(answer_from_bot))
    talk(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)

frame=Frame(main)

sc=Scrollbar(frame)
msgs= Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT,fil=BOTH, pady=10)

frame.pack()

#text field

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn=Button(main,text="Ask from alexa", font=("Verdana",20), command=ask_from_alexa)
btn.pack()

#creating a function

def enter_function(event):
    btn.invoke()

#To bind main window with enter key..

main.bind('<Return>', enter_function)

def repeatL():
    while True:
        take_query()

t=threading.Thread(target=repeatL)

t.start()

main.mainloop()