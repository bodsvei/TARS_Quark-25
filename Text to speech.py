import pyttsx3

def speak(text):
  """
  Converts the given text to speech using pyttsx3.

  Args:
    text: The text to be spoken.
  """
  engine = pyttsx3.init() 
  engine.say(text)
  engine.runAndWait() 

# Example usage:
while True:
  user_input = input("Enter text to speak (or 'exit' to quit): ")
  if user_input.lower() == 'exit':
    break
  speak(user_input)