from multiprocessing import Process
import time
# 父进程 n=100
n = 100


def task(name):
    global n
    n = 0
    time.sleep(5)
    # 如果n=0使得最后主进程打印不为0，则说明内存是互相隔离的


if __name__ == '__main__':
    p = Process(target=task, args=('alex',))
    # 给系统发信号，申请内存空间，启子进程
    p.start()
    # p.join 表示子进程运行完，才运行主进程
    print(p.is_alive())
    p.join()
    
    print('主', n)
