import socket
import struct

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
while True:

    # 发收消息
    cmd = input('>>>>:')
    if not cmd:
        continue
    client.send(cmd.encode('utf-8'))

    headers = client.recv(4)
    total_size = struct.unpack('i', headers)
    print(total_size)
    # print('发送了：%s' % cmd)
    # 收消息
    # data = client.recv(1024)
    # print('收到了：%s' % data)


# 挂电话连接
client.close()
