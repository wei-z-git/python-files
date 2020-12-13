from multiprocessing import Process
import time
import os

# ppid 爹的进程号
def task(n):
    print('pid is %s ppid is %s ' % (os.getpid(),os.getppid()))
    time.sleep(n)



if __name__ == '__main__':
    p=Process(target=task,args=(100,))
    p.start()
    # p.terminate()
    print(p.is_alive())
    p.name='haha'
    print(p.name)
    time.sleep(100)
    print('主ppid is %s'%(os.getppid()))
