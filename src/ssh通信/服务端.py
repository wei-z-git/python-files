from socket import AF_INET, SOCK_STREAM, socket
import subprocess

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8090))
server.listen(5)

while True:
    print('starting...')
    conn, client_addr = server.accept()
    print(client_addr)

    while True:
        try:
            cmd = conn.recv(1024)
            if not cmd:
                break
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE
                                   )
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            conn.send(stdout+stderr)
        except ConnectionResetError:
            break

    conn.close()
server.close()
