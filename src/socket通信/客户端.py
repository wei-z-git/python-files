import socket


# 买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 打电话
phone.connect(('127.0.0.1', 8080))
while True:

    # 发收消息
    msg = input('>>>>:')
    phone.send(msg.encode('utf-8'))
    print('发送了：%s' % msg)
    # 收消息
    data = phone.recv(1024)
    print('收到了：%s' % data)


# 挂电话连接
phone.close()
