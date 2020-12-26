from socket import *
from threading import current_thread, Thread


def client():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('127.0.0.1', 8080))
    while True:
        # client.send('say hello'.encode('utf-8'))
        client.send('say hello'.encode('utf-8'))
        print('send')
        data = client.recv(1024)
        print(data.decode('utf-8'))

    client.close() 
if __name__ == "__main__":
    for i in range(10):
        t=Thread(target=client)
        t.start()
