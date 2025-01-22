import ollama

client = ollama.Client()

model = "llama3.2:1b"
r = client.generate(model = model, prompt = "You are TARS our projrct for the Electronics and Robotics Club. Reply in 1-2 lines with humorous responses.")


while True:
    prompt = input("Speak : ")
    prompt += ". Reply in 1-2 lines."
    f = open("brains\llm_out.txt", "a")

    r = client.generate(model = model, prompt = prompt)
    print("-*-*-*-*-*-*-*-*-*-*-")
    print(r.response)
    
    f.write(r.response)
    f.close()