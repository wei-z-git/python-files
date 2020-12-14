# from threading import Thread
# import time
# import random
# import os


# def piao():
#     print('%s is piaoing' % os.getpid())
#     time.sleep(random.randint(1, 3))


# if __name__ == '__main__':
#     t1 = Thread(target=piao,)
#     t2 = Thread(target=piao,)
#     t3 = Thread(target=piao,)
#     t1.start()
#     t2.start()
#     t3.start()
#     print('主', os.getpid())


# 同一个进程不同线程pid都一样
# 共享同样的全局变量
from  threading import Thread
from multiprocessing import Process
import os
def work():
    global n
    n=0

if __name__ == '__main__':
    # n=100
    # p=Process(target=work)
    # p.start()
    # p.join()
    # print('主',n) #毫无疑问子进程p已经将自己的全局的n改成了0,但改的仅仅是它自己的,查看父进程的n仍然为100


    n=1
    t=Thread(target=work)
    t.start()
    t.join()
    print('主',n) #查看结果为0,因为同一进程内的线程之间共享进程内的数据

