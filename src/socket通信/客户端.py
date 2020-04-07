import socket


# 买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 打电话
phone.connect(('127.0.0.1', 8080))

# 发收消息
a = 'hello'
phone.send(a.encode('utf-8'))
print('发送了：%s' % a)
# 收消息
data = phone.recv(1024)


# 挂电话连接
phone.close()
