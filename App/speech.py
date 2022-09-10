import speech_recognition as sr
from playsound import playsound
import time
import gtts
import os


# def function_sound():
#     playsound('C:/Users/michj/Desktop/Thesis/hello.mp3')


def speak(text):
    tts = gtts.gTTS(text, lang='en')
    tts.save('hello.mp3')
    playsound('hello.mp3')
    # time.sleep(1)
    os.remove('hello.mp3')


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        # r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        try:
            statement = r.recognize_wit(audio,'BP5JXWTCZP7KWAVXAYPEO5QDW77HKOYU' , show_all = False)
            print(f"user said:{statement}\n")

        except Exception as e:
            # speak("Pardon me, please say that again")
            return "None"
        return statement
