from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3
import speech_recognition as sr
import threading

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(talk):
    engine.say(talk)
    engine.runAndWait()

bot = ChatBot("alexa")

convo=[
    'Hello',
    'hi there!',
    'What is your name?',
    'My name is alexa, I am created by Tinesh',
    'How are you ?',
    'I am doing great these days',
    'Thank you',
    'In which city you live ?',
    'I live in Chennai',
    'In which language you talk?',
    'I mostly talk in english'
]

trainer = ListTrainer(bot)

# #Train with trainers

trainer.train(convo)


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

def takeQuery():
    listener = sr.Recognizer()
    listener.pause_threshold=1
    print("Alexa is listening ...")
    with sr.Microphone() as source:
        try:
            voice = listener.listen(source)
            query = listener.recognize_google(voice, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
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
        takeQuery()
t=threading.Thread(target=takeQuery)

t.start()

main.mainloop()