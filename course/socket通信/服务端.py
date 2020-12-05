import socket

# 买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定手机
phone.bind(('127.0.0.1', 8080))

# 开机
phone.listen(5)

# 等待连接
print('starting...')
while True:

    conn, client_addr = phone.accept()  # (conn,client_addr)
    print(client_addr)

    # 收发消息
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break  # 针对linux，防止死循环
            print('收到客户端消息：%s' % data)
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()

# 关机
phone.close()
