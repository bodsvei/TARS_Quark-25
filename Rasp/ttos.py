import pyttsx3

f=open("llm_out.txt", "r")
engine = pyttsx3.init()
while True:
  _in = f.read()
  engine.say(_in)
  engine.runAndWait() 
  
