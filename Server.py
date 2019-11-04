import socket, select, threading
from _thread import *

IP = "127.0.0.1"
Port = 5555
MSG_HEADER = 10
lock = threading.Lock()
socketList = []
clientsList = []

def thread(client):
    while True:
        data = client.recv(1024)
        if not data:
            print('end')
            lock.relase()
            break
        
        data = data[::-1]
        client.send(data)
    client.close()

def main():
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ServerSocket.bind((IP, Port))
    print(f"Server Socket binded at {IP}:{Port}")
    ServerSocket.listen()
    socketList = [ServerSocket]
    clientsList = {}
    print("Socket is listening...")
    while True:
        client, info = ServerSocket.accept()
        lock.acquire()
        print(f"Connected to {info[0]}:{info[1]}")
        start_new_thread(thread(client))
    ServerSocket.close()

main()