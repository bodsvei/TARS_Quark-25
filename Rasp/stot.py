import speech_recognition as sr

r=sr.Recognizer()

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


def writeText(text, f):
    f.write(text)
    f.write("\n")
    f.close


while(1):
    text = recordText()
    print(text)
    out = writeText(text)

    print("out.txt UPDATED")


if __name__ == "__main__":
    recordText()
    writeText()
