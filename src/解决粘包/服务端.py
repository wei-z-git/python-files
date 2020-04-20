from socket import AF_INET, SOCK_STREAM, socket
import subprocess
import struct

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

            # 制作固定长度报头，用struct吧totalsize打包成4bytes的
            total_size = len(stdout)+len(stderr)
            headers = struct.pack('i', total_size)

            conn.send(headers)
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:
            break

    conn.close()
server.close()
