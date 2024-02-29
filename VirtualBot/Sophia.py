import pyttsx3 as pt
import speech_recognition as sophia
import pywhatkit
import datetime
import wikipedia
import requests
import webbrowser
import os
import random
import smtplib
import math
import re

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    instruction = ""

    try:
        print("Listening...")  
        with sophia.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)
            instruction = listener.recognize_wit(audio, key="V5P26ITKTZEGWTKEA2UMQCYGCE4VVNWX")
            instruction = instruction.lower()
            if "sophia" in instruction:
                instruction = instruction.replace('sophia', "")
                print(instruction)
                # Extract city name using regex
                city_match = re.search(r'in (\w+)', instruction)
                if city_match:
                    city_name = city_match.group(1)
                    print("Extracted City Name:", city_name)  # Debugging: Print the extracted city name
                    return instruction, city_name  # Return both the instruction and the extracted city name
            
    except sophia.UnknownValueError:
        print("Sophia could not understand audio")
    except sophia.RequestError as e:
        print("Could not request results from Sophia; {0}".format(e))
    except Exception as e:
        print("An error occurred:", e)
        
    return instruction, None



def play_Sophia():
    while True:
        instruction, city_name = input_instruction()
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
            
        elif any(word in instruction for word in ['how are you', 'how you doing']):
            talk('I am great, how about you?')
            
        elif any(word in instruction for word in ['what is your name', 'whats your name', 'what\'s your name']):
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
        
        elif 'send email' in instruction:
            try:
                talk("What should I say?")
                content, _ = input_instruction()
                talk("Who should I send it to?")
                recipient, _ = input_instruction()

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login('your_email@gmail.com', 'your_password')
                server.sendmail('your_email@gmail.com', recipient, content)
                server.close()
                talk('Email has been sent successfully!')
            except Exception as e:
                print(e)
                talk('Sorry! I am unable to send your email at the moment.')
        
        elif 'open website' in instruction:
            talk('Sure, which website would you like me to open?')
            website, _ = input_instruction()
            webbrowser.open_new_tab('https://' + website + '.com')

        elif 'open application' in instruction:
            talk('Sure, which application would you like me to open?')
            application, _ = input_instruction()
            os.system("start " + application)

        elif 'tell me a joke' in instruction:
            jokes = ["Why don't scientists trust atoms? Because they make up everything!", 
                     "I told my wife she was drawing her eyebrows too high. She looked surprised!", 
                     "What do you call fake spaghetti? An impasta!"]
            talk(random.choice(jokes))

        elif 'thank you' in instruction:
            talk('You are welcome!')

        elif 'stop' in instruction or 'exit' in instruction:
            talk('Goodbye!')
            break

        # New features
        elif 'weather' in instruction:
            api_key = "YOUR_OPENWEATHERMAP_API_KEY"
            weather = get_weather(api_key, city_name)
            talk(weather)

        elif 'news' in instruction:
            news = get_news()
            talk(news)

        elif 'stock price' in instruction:
            stock_price = get_stock_price()
            talk(stock_price)

        elif 'define' in instruction:
            word = instruction.replace('define', '').strip()
            definition = get_definition(word)
            talk(definition)

        elif 'translate' in instruction:
            translation = translate_instruction(instruction)
            talk(translation)

        elif 'calculate' in instruction:
            calculation = calculate_instruction(instruction)
            talk(calculation)

        elif 'convert' in instruction:
            conversion = convert_instruction(instruction)
            talk(conversion)

        elif 'remind me' in instruction:
            reminder = set_reminder(instruction)
            talk(reminder)

        elif 'set timer' in instruction:
            timer = set_timer(instruction)
            talk(timer)

        elif 'find' in instruction:
            location = find_location(instruction)
            talk(location)

        elif 'tell me a fact' in instruction:
            fact = get_random_fact()
            talk(fact)

        else:
            talk('I couldn\'t catch that. Do you have any more instructions?')

        # Ask the user if they have more requests
        more_instructions = input("Do you have more instructions? (yes/no): ").lower()
        if more_instructions != 'yes':
            break
        
def get_weather(api_key, city_name):
    api_key = "5b4d35aee898e32964e2b6d7bdf56877"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    print("URL:", url)  # Debugging: Print the URL being requested
    response = requests.get(url)
    print("Response:", response.json())  # Debugging: Print the JSON response
    
    weather_data = response.json()
    if response.status_code == 200:
        description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        weather_info = f"The weather in {city_name} is {description} with a temperature of {temperature} degrees Celsius."
        return weather_info
    else:
        return "Failed to fetch weather data."

def get_news():
    # Use news API to fetch news headlines
    response = requests.get("https://api.news.com/")
    news_data = response.json()
    # Extract relevant information from the response
    headlines = [headline["title"] for headline in news_data["headlines"]]
    news_info = "Here are the latest news headlines: " + ", ".join(headlines)
    return news_info

def get_stock_price():
    # Use stock market API to fetch stock prices
    response = requests.get("https://api.stock.com/")
    stock_data = response.json()
    # Extract relevant information from the response
    stock_info = "The current stock price of ABC Corporation is " + str(stock_data["price"]) + " dollars."
    return stock_info

def get_definition(word):
    # Use dictionary API to fetch the definition of a word
    response = requests.get(f"https://api.dictionary.com/definition/{word}")
    definition_data = response.json()
    # Extract relevant information from the response
    definition = definition_data["definitions"][0]["definition"]
    return definition

def translate_instruction(instruction):
    # Use translation API to translate the instruction to another language
    translation = "Translated instruction..."
    return translation

def calculate_instruction(instruction):
    # Parse and evaluate the mathematical expression in the instruction
    try:
        result = eval(instruction.replace('calculate', '').strip())
        return str(result)
    except Exception as e:
        return "Sorry, I couldn't calculate that."

def convert_instruction(instruction):
    # Implement conversion logic here
    return "Conversion result..."

def set_reminder(instruction):
    # Implement reminder setting logic here
    return "Reminder set successfully!"

def set_timer(instruction):
    # Implement timer setting logic here
    return "Timer set successfully!"

def find_location(instruction):
    # Implement location finding logic here
    return "Location found..."

def get_random_fact():
    # Implement random fact retrieval logic here
    return "Random fact..."

listener = sophia.Recognizer()
machine = pt.init()

voices = machine.getProperty('voices')
machine.setProperty('voice', voices[1].id)

play_Sophia()
