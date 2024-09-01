print('Welcome to the Alexa Project')

import speech_recognition as sr
import pyttsx3 
import pywhatkit
import wikipedia
from datetime import datetime
import pyjokes
from Py_Weather import get_weather
import os
import random
import math
import time

r = sr.Recognizer()

def talk(answer):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(answer)
    engine.runAndWait()

def get_question():
    with sr.Microphone() as source:
        print('Say Something')
        audio = r.listen(source)

        try:
            question = r.recognize_google(audio)
            print(f'You said: {question}')
            
            if 'Alexa' in question:
                question = question.replace('Alexa', '')
                print(f'Processing your request: {question}')
                return question
            else:
                print('Not addressing me, no action taken.')
                return 'notwithme'
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand. Please try again.")
            return 'notunderstood'

def process_question(question):
    if 'what are you doing' in question:
        response = 'I am waiting for your question'
        print(response)
        talk(response)
        return True
        
    elif 'how are you' in question:
        response = 'I am good, thank you. How can I help you?'
        print(response)
        talk(response)
        return True

    elif 'play' in question:
        query = question.replace('play', '')
        response = f'Playing {query} on YouTube.'
        print(response)
        talk(response)
        pywhatkit.playonyt(query)
        return True

    elif 'who is' in question:
        query = question.replace('who is', '')
        summary = wikipedia.summary(query, sentences=2)
        print(summary)
        talk(summary)
        return True

    elif 'joke' in question:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
        return True

    elif 'date' in question or 'time' in question:
        if 'time' in question:
            current_time = datetime.now().strftime('%I:%M %p')
            print(f'The current time is {current_time}')
            talk(f'The current time is {current_time}')
            return True
        
        if 'date' in question:
            current_date = datetime.now().strftime('%B %d, %Y')
            print(f'Today\'s date is {current_date}')
            talk(f'Today\'s date is {current_date}')
            return True

    elif 'weather' in question:
        weather = get_weather()
        print(weather)
        talk(weather)
        return True

    elif 'your name' in question:
        response = 'I am your voice assistant, you can call me Alexa.'
        print(response)
        talk(response)
        return True

    elif 'created you' in question or 'who made you' in question:
        response = 'I was created by a team of developers who love to code!'
        print(response)
        talk(response)
        return True

    elif 'open notepad' in question:
        os.system('notepad')
        response = 'Opening Notepad'
        print(response)
        talk(response)
        return True

    elif 'roll a dice' in question:
        dice_roll = random.randint(1, 6)
        response = f'The dice rolled a {dice_roll}'
        print(response)
        talk(response)
        return True

    elif 'square root' in question:
        number = float(question.replace('square root', '').strip())
        sqrt = math.sqrt(number)
        response = f'The square root of {number} is {sqrt}'
        print(response)
        talk(response)
        return True

    elif 'set a timer' in question:
        seconds = int(question.replace('set a timer for', '').strip().split()[0])
        response = f'Setting a timer for {seconds} seconds'
        print(response)
        talk(response)
        time.sleep(seconds)
        talk('Time is up!')
        return True
        
    elif 'bye' in question:
        talk('Goodbye! Take care, we will meet later.')
        return False

    else:
        response = "I'm sorry, I couldn't understand your request. Could you ask me again?"
        print(response)
        talk(response)
        return True

askquestion = True
while askquestion:
    question = get_question()
    if question == 'notwithme':
        talk('Ok, carry on with your friends. Goodbye!')
        askquestion = False
    elif question == 'notunderstood':
        talk("I couldn't catch that. Could you please repeat?")
    else:
        askquestion = process_question(question)
