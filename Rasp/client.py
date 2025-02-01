import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print ("Socket successfully created")

IP="0.0.0.0"
port = 8000

s.connect(IP, port)

def requestLLMOut():
    msg=s.recv(8)
    return msg
