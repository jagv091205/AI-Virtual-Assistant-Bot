import speech_recognition as Luna
from gtts import gTTS
import playsound
import os

# Converting speech to text so that we can use text for the next step
def luna_listen():
    s = Luna.Recognizer() # created a recognizer
    with Luna.Microphone() as source: # whatever we will speak on the microphone should act as our source
        audio = s.listen(source) # use the listen function so the recognizer can catch the source which is our mic.
        text=''
        try:
            print('listening...')
            text = s.recognize_wit(audio, key="V5P26ITKTZEGWTKEA2UMQCYGCE4VVNWX")
        except Luna.RequestError as re:
            print(re)
        except Luna.UnknownValueError as uve:
            print(uve)
        except Luna.WaitTimeoutError as wte:
            print(wte)
    text = text.lower()
    return text

# Converting text to speech
def luna_talk(text):
    file_name = 'audio.mp3' # corrected the file extension
    tts = gTTS(text=text, lang='en') # converted text to speech
    tts.save(file_name) # save file
    playsound.playsound(file_name) # play file without extension
    os.remove(file_name) # remove file

def luna_reply(text):
    if 'what' in text and 'name' in text:
        luna_talk('I am Luna and I am your personal assistant!')
   
    elif 'when' in text and 'exists' in text:
        luna_talk('''I was created to work for you. I don't need a break and I will never ask for days off!''')
        
    elif 'when' in text and 'sleep' in text:
        luna_talk('''I never sleep. I was created to support you 24 hours and 7 days a week''')
        
    elif 'you' in text and 'stupid' in text:
        luna_talk('''No I am not stupid. My grandmother told me that there are no stupid persons out there. I try to give my best everyday and learn continuously.''')
        
    elif 'favorite' in text or 'favourite' in text and 'movie' in text:
        luna_talk("My favorite move is Titanic. I watch it with my friends all the time")
      
    elif 'stop' in text:
        luna_talk('It was my pleasure to help you. I wish you have a wonderful day ahead')
          
    else:
        luna_talk('''Am Sorry but I couldn't get that. Can you please repeat it?''')

# Luna Execution Section
def execute_assistant():
    
    #personalization
    luna_talk('Hi, I am Luna and I am here to support you. Can you please tell me your name?')
    listen_name = luna_listen() # Call the function to get the user's name
    luna_talk('Hello ' + listen_name + ', what can I do for you today?') # Concatenate the name with the greeting
    
    while True:
        listen_luna = luna_listen()
        print(listen_luna)
        luna_reply(listen_luna)
        if 'stop' in listen_luna: # stop keyword is used then the while loop and Luna will stop executing
            break

execute_assistant()
