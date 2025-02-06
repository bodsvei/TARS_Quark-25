import socket
from os import _exit
from threading import Thread


class Client:

    def __init__(self, HOST, PORT):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(HOST, PORT)

        self.TalkToServer()

    def TalkToServer(self):
        Thread(target=self.recieveMessage).start()
        self.sendMessage()
    
    def sendMessage(self, client_socket):
        while True:
            clientMessage=input(" ")
            client_socket.send(clientMessage.encode())

    def recieveMessage(self):
        while True:
            sMsg = self.socket.recv(1024).decode()
            if (sMsg == "bye" or not sMsg.strip()):
                _exit(0)
            print("\033[1;31;40m" + "TARS: " + sMsg + "\033[0m")

if __name__ == "__main__":
    Client

s.connect((IP, port))

def requestLLMOut():
    msg=s.recv(8)
    return msg

