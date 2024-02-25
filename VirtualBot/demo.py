import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Listening...")
        audio = listener.listen(source)
        print("Recognizing...")
        text = listener.recognize_wit(audio, key="V5P26ITKTZEGWTKEA2UMQCYGCE4VVNWX")
        print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand what you said.")
except sr.RequestError as e:
    print("Could not request results from Wit.ai; {0}".format(e))
