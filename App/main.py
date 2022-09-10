from scraper import getTasks
from speech import takeCommand
from speech import speak
from youtube import playYoutube
from message import sendMail
import datetime
import wikipedia
import time


print("Loading your personal assistant pi")
speak("Loading your personal assistant pi")

if __name__ == '__main__':

    while True:
        statement = takeCommand().lower()
        print(statement)
        if statement == 'hello pi' or statement == 'hello bi' or statement == 'hello pie' or statement == 'hello bye':
            speak("What can i do for you?")
            while 'stop' not in statement:
                statement = takeCommand().lower()

                if 'tasks' in statement:
                    tasks = getTasks()
                    speak(f'You have {len(tasks)} tasks')
                    for i in tasks:
                        print(i)
                        speak(i)
                    break

                elif 'time' in statement:
                    time = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f'It is {time} right now')
                    speak(f'It is {time} right now')
                    break

                

                elif 'play' in statement:
                    statement = statement.replace('play', '')
                    if statement == '':
                        break
                    playYoutube(statement)
                    break

                elif 'send mail to' in statement:
                    statement = statement.replace('send mail to ', '')
                    if statement == 'dad':
                        recipient = 'michja144+test1@gmail.com'
                    elif statement == 'mom':
                        recipient = 'michja144+test2@gmail.com'
                    speak(f'what should the title be')
                    statement = takeCommand().lower()
                    title = statement
                    speak('what should the content be')
                    statement = takeCommand().lower()
                    message = statement
                    sendMail(title, message, recipient)

                elif 'what is' in statement:
                    statement = statement.replace("what is", "")
                    if statement == "":
                        break
                    results = wikipedia.summary(statement, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                    break