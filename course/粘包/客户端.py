from socket import AF_INET, SOCK_STREAM, socket
import time

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

client.send('hello'.encode('utf-8'))
time.sleep(5)
client.send('hello'.encode('utf-8'))
client.close()
