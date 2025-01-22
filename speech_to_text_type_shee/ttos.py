from gtts import gTTS

f=open("llm_out.txt", "r")
flag = True

while flag:
    r=f.read()
    language ="en"

    aud = gTTS(text=r, lang=language, slow=False)
    aud.save("audio.mp3")

    flag = False

