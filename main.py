import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(talk):
    engine.say(talk)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Say Something...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:                        
                print(command)
                command = command.replace('alexa', '')
            else:
                print('Say Alexa')
                talk('Say Alexa')
                
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song )
        print('playing')

run_alexa()