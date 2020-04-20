from socket import AF_INET, SOCK_STREAM, socket
import struct


client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8090))

while True:
    cmd = input('>>:').strip()
    if not cmd:
        continue

    client.send(cmd.encode("utf-8"))
    # 先接受报头

    headers = client.recv(4)
    total_size = struct.unpack('i', headers)[0]

    recv_size = 0
    data = b''
    while recv_size < total_size:
        recv_data = client.recv(1024)
        data += recv_data
        recv_size += len(recv_data)
    print(data.decode('gbk'))
client.close()
