import socket

IP="0.0.0.0"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, 8000))
s.listen(5)

f=open("llm_out.txt", "a")

while True:
    clientSocket, adress = s.accept()
    print(f"Connection from {adress} has been established")
    clientSocket.send(bytes("Welcome to server!", "utf8"))
    clientSocket.send(bytes(f.readline(), "utf8"))