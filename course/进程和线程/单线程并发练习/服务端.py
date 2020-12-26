import gevent
from socket import *
from threading import current_thread
from gevent import monkey, spawn
monkey.patch_all()


def communicate(conn):
    print('子线程：%s'%current_thread().getName())
    while True:
        try:
            data=conn.recv(1024)
            conn.send(data.upper())
        except ConnectionResetError:
            break
        conn.close()

def server(server_ip, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((server_ip, port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print(addr)
        # 实例一个communicate的协程
        spawn(communicate, conn)
        # 这里不需要j.join了

  



if __name__ == '__main__':
    # spawn提交server的任务
    g=spawn(server,'127.0.0.1', 8080)
    g.join()
