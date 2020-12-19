# 计算密集型，多进程效率高
from threading import Thread
from multiprocessing import Process
import time


def work():
    res=2
    for i in range(100000000):
        res*=i


if __name__ == '__main__':
    start = time.time()
    l = []
    for i in range(4):
        # p = Thread(target=work) #耗时13.705921411514282
        p = Process(target=work) #耗时3.5441336631774902


        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop = time.time()
    print("run time is %s" % (stop-start))
