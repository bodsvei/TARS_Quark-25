import socket
import ollama
import pyttsx3
from os import _exit
from threading import Thread


class Server:

    def __init__(self, HOST, PORT):
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((HOST, PORT))

        self.socket.listen()
        print("Server waiting for connection ...")

        clientSocket, adress = self.socket.accept()
        print("Handshake from:"+str(adress))

        self.TalkToCLient(clientSocket)

    def TalkToClient(self, client_socket):
        Thread(target=self.recieveMessage, args=(client_socket,)).start()
    
    def sendMessage(self, client_socket):
        while True:
            serverMessage=input("")
            client_socket.send(serverMessage.encode())

    def recieveMessage(self, client_socket):
        while True:
            cMsg = client_socket.recv(1024).decode()
            if (cMsg == "bye" or not cMsg.strip()):
                _exit(0)
            print("\033[1;31;40m" + "User: " + cMsg + "\033[0m")

if __name__ == "__main__":
    Server