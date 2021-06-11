import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import time

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(talk):
    engine.say(talk)
    engine.runAndWait()

def take_query():
    with sr.Microphone() as source:        
        print('Say Something...')
        talk('Say Something...')
        voice = listener.listen(source)
        try:
            query = listener.recognize_google(voice)
            query = query.lower()                        
            print(query)
            query = query.replace('alexa', '')
        except sr.UnknownValueError:
            print('Sorry, I did not get that')
            pass
        return query

def run_alexa():
    query = take_query()
    print(query)
    if 'play' in query:
        song = query.replace('play', '')
        talk('playing' + song )
        pywhatkit.playonyt(song)
    elif ('time') in query:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print('The current time is: '+ time)
        talk('The current time is: '+ time)
    elif 'wikipedia' in query:
        person= query.replace('wikipedia','')
        info= wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in query:
        talk(pyjokes.get_joke)
    elif 'search' in query:
        search= query.replace('search', '')
        url= 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what I found ' + search)
        talk('Here is what I found')
    elif ('Find' and 'Location') or ('Location' or 'Located') in query:
        location= query.replace('Location', '')
        url= 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Here is the location ' + search)
        talk('Here is the location')
    else:
        print('Say it again')
        talk('Say it again')

time.sleep(1)
while 1:
    run_alexa()