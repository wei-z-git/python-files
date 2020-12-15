from threading import Thread,current_thread
from socket import *


def comunicate(conn):
    print('子线程:%s'%current_thread().getName())
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()


def server(ip, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print('主线程:%s'%current_thread().getName())

    while True:
        conn, addr = server.accept()
        print(addr)
        # 主线程还是启监听，每启动一个监听则一个子线程建立通信
        t=Thread(target=comunicate,args=(conn,))
        t.start()

        # comunicate(conn)
    server.close()


if __name__ == '__main__':
    server('127.0.0.1', 8080)
