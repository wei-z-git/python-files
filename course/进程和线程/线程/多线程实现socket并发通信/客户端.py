from socket import *


client = socket(AF_INET, SOCK_STREAM)


client.connect(('127.0.0.1', 8080))
while True:

    msg = input('>>>>:')
    if not msg:
        continue
    client.send(msg.encode('utf-8'))
    print('发送了：%s' % msg)
    data = client.recv(1024).decode('utf-8')
    print('收到了：%s' % data)



client.close()
