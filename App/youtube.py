import pywhatkit
import os


def stopYoutube():
    os.system('taskkill /im chrome.exe /f')


def playYoutube(name):
    stopYoutube()
    pywhatkit.playonyt(name, True)
