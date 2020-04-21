from socket import AF_INET, SOCK_STREAM, socket
import struct
import json

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8090))

while True:
    cmd = input('>>:').strip()
    if not cmd:
        continue

    client.send(cmd.encode("utf-8"))
    # 先接受报头长度

    header_lenth = client.recv(4)
    header_size = struct.unpack('i', header_lenth)[0]

    # 接受报头
    header_bytes = client.recv(header_size)
    header_json = header_bytes.decode('utf-8')
    header_dic = json.loads(header_json)
    print('====>', header_dic)
    total_size = header_dic['total_size']

    recv_size = 0
    data = b''  # 规定data的类型为byte
    while recv_size < total_size:
        recv_data = client.recv(1024)
        data += recv_data
        recv_size += len(recv_data)
    print(data.decode('gbk'))
client.close()
