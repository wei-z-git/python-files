import socket

# 买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定手机
phone.bind(('127.0.0.1', 8080))

# 开机
phone.listen(5)

# 等待连接
print('starting...')
conn, client_addr = phone.accept()  # (conn,client_addr)
print(conn, client_addr)

# 收发消息
while True:

    data = conn.recv(1024)
    conn.send(data.upper())

# 挂电话
conn.close()

# 关机
phone.close()
