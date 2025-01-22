import ollama

client = ollama.Client()

model = "llama3.2:1b"

while True:
    prompt = input("Speak : ")

    r = client.generate(model = model, prompt = prompt)

    print("---------------")
    print(r.response)


