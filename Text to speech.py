import pyttsx3

def speak(text):
  engine = pyttsx3.init() 
  engine.say(text)
  engine.runAndWait() 

# Example usage:
while True:
  user_input = input("Enter text to speak (or 'exit' to quit): ")
  if user_input.lower() == 'exit':
    break
  speak(user_input)