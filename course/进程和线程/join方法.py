from multiprocessing import Process
import time
import os


def task(n):
    print('%s is running ' % os.getpid())
    time.sleep(n)
    print('%s is done' % os.getpid)


if __name__ == '__main__':
    p1=Process(target=task,args=(1,))
    p2=Process(target=task,args=(2,))
    p3=Process(target=task,args=(3,))
    start_time=time.time()
    p1.start()
    p2.start()
    p3.start()

# 主进程等p1
    p1.join()
    p2.join()
    p3.join()
    stop_time=time.time()
    print('主',(stop_time-start_time))
