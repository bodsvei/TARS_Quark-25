from stot import recordText
from client import requestLLMOut
import time
import pyttsx3

engine = pyttsx3.init()

while True:
    text = recordText()
    print(text)
    time.sleep(2)
    engine.say(requestLLMOut())
    engine.runAndWait()

