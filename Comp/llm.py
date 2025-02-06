import ollama
import pyttsx3
import speech_recognition as sr


def recordText():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                _text = r.recognize_google(audio2)

                return _text

        except sr.RequestError as e:
            print("Could not request results:{0}".format(e))

        except:
            print("Unknown errors encountered")

    return _text

IP="192.168.130.76"

r=sr.Recognizer()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = ollama.Client()
eng = pyttsx3.init()

s.bind((IP, 8000))
s.listen(5)

model = "llama3.2:3b"
flag=True

while True:
    if flag:
        clientSocket, adress = s.accept()
        print(f"Connection from {adress} has been established")
        flag = False
    prompt = input("Speak : ")
    prompt = "Act like TARS from the movie Interstellar. Reply in 1 to 2 line. " + prompt
    r = client.generate(model = model, prompt = prompt)
    print("-*-*-*-*-*-*-*-*-*-*-")
    clientSocket.send(bytes(r.response, "utf8"))
    eng.say(r.response)
    eng.runAndWait()
    print(r.response)