import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

def listen_for_keyword():
    """Listen for the 'hello' or 'bye' keyword."""
    with sr.Microphone() as source:
        print("Waiting for 'hello' to start listening or 'bye' to exit...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        while True:
            try:
                audio = recognizer.listen(source, timeout=None)  # Listen indefinitely
                command = recognizer.recognize_google(audio).lower()
                if "hello" in command:
                    print("Detected 'hello'! Starting to listen...")
                    return True
                elif "bye" in command:
                    print("Detected 'bye'! Exiting...")
                    return False
            except sr.UnknownValueError:
                print("Could not understand. Please say 'hello' or 'bye'.")

def transcribe_speech():
    """Continuously transcribe speech until 'bye' is detected."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Say 'bye' to stop.")
        while True:
            try:
                audio = recognizer.listen(source, timeout=None)
                text = recognizer.recognize_google(audio).lower()
                if "bye" in text:
                    print("Detected 'bye'! Stopping...")
                    break
                print(f"You said: {text}")
            except sr.UnknownValueError:
                print("Could not understand. Please try again.")
            except sr.RequestError:
                print("There was an error with the request. Please check your internet connection.")

# Main loop
while True:
    start = listen_for_keyword()
    if start:
        transcribe_speech()
    else:
        break
