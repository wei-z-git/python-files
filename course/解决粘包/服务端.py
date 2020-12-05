from socket import AF_INET, SOCK_STREAM, socket
import subprocess
import struct
import json

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8090))
server.listen(5)

while True:
    print('starting...')
    conn, client_addr = server.accept()
    print(client_addr)

    while True:
        try:
            cmd = conn.recv(8096)
            if not cmd:
                break
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE
                                   )
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            headers = {
                'filepath': 'a.txt',
                'md5': '123xxasd2asdfg',
                'total_size': len(stdout)+len(stderr)
            }
            headers_json = json.dumps(headers)
            headers_bytes = headers_json.encode('utf-8')

            # 发送报头长度

            conn.send(struct.pack('i', len(headers_bytes)))

            # 再发报头

            conn.send(headers_bytes)
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:
            break

    conn.close()
server.close()
