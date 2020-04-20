from socket import AF_INET, SOCK_STREAM, socket
import time

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)
print('starting...')


conn, addr = server.accept()
res1 = conn.recv(10)
print('', res1)
time.sleep(6)
res2 = conn.recv(10)
print('', res2)
conn.close()
server.close()
