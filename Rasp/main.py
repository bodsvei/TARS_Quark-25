from stot import recordText, writeText
from client import requestLLMOut
import time
import pyttsx3

engine = pyttsx3.init()

while True:
    text = recordText()
    print(text)
    out = writeText(text)
    requestLLMOut()
    time.sleep(2)
    engine.say(requestLLMOut())
    engine.runAndWait()

