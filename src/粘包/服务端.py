from socket import AF_INET, SOCK_STREAM, socket

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8090))
server.listen(5)

conn, client_addr = server.accept()
print(client_addr)
res1 = conn.recv(10)
print('res1:', res1)
res2 = conn.recv(10)
print('res2:', res2)
conn.close()
server.close()
