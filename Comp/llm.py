import ollama

client = ollama.Client()

model = "llama3.2:1b"

while True:
    prompt = input("Speak : ")
    prompt += ". Reply in 1-2 lines."
    f = open("llm_out.txt", "a")

    r = client.generate(model = model, prompt = prompt)
    print("-*-*-*-*-*-*-*-*-*-*-")
    print(r.response)
    
    f.write(r.response)
    f.write("\n")
    f.close()