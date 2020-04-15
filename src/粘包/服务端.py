import socket
import subprocess
import struct

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)
print('starting...')

while True:

    conn, client_addr = server.accept()  # (conn,client_addr)
    print(client_addr)

    # 收发消息
    while True:
        try:
            cmd = conn.recv(8096)
            if not cmd:
                break  # 针对linux，防止死循环
            # 制作固定长度报头
            stdout=obj.stdout.read()
            stderr=obj.stderr.read()
            total_size = len(stdout)+len(stdout)
            headers = struct.pack('i', total_size)
            print('收到客户端消息：%s' % cmd)
            conn.send(cmd.upper())
        except ConnectionResetError:
            break
    conn.close()

# 关机
server.close()
