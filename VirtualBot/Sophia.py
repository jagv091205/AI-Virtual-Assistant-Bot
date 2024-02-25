import speech_recognition as sophia
import pyttsx3 as pt
import pywhatkit
import datetime
import wikipedia

listener = sophia.Recognizer()
machine = pt.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    instruction = ""

    try:
        print("listening...")  # Moved print statement here
        with sophia.Microphone() as origin:
            speech = listener.listen(origin)
            instruction = listener.recognize_wit(speech, key="V5P26ITKTZEGWTKEA2UMQCYGCE4VVNWX")
            instruction = instruction.lower()
            if "Sophia" in instruction:
                instruction = instruction.replace('Sophia', "")
                print(instruction)
            
    except sophia.UnknownValueError:
        print("Sophia could not understand audio")
    except sophia.RequestError as e:
        print("Could not request results from Sophia; {0}".format(e))
    except Exception as e:
        print("An error occurred:", e)
        
    return instruction


def play_Sophia():
    instruction = input_instruction()
    print(instruction)
    
    if "play" in instruction:
        song = instruction.replace('play', "")
        talk("Playing "+ song)
        pywhatkit.playonyt(song)
        
    elif 'time' in instruction:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is '+ current_time)
        
    elif 'date' in instruction:
        current_date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Today's date is " + current_date)
        
    elif 'how are you' in instruction or 'how you doing' in instruction:
        talk('I am great, how about you?')
        
    elif 'What is your name' in instruction or 'Whats your name' in instruction or '''What's your name''' in instruction:
        talk('I am Sophia! Nice to meet you! What can I do for you today?')
    
    elif 'who is' in instruction:
        person = instruction.replace('who is ', "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    
    elif 'what is' in instruction:
        obj = instruction.replace('what is ', "")
        info = wikipedia.summary(obj, 1)
        print(info)
        talk(info)
        
    else:
        talk('I couldn\'t catch that. Can you please repeat?')

play_Sophia()
