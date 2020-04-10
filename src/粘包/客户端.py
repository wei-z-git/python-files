from socket import AF_INET, SOCK_STREAM, socket

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8090))

client.send('hello'.encode('utf-8'))
client.send('world'.encode('utf-8'))


client.close()
