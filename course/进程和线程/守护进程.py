from multiprocessing import Process
import time


def task(name):
    p = Process(target=time.sleep, args=(6,))
    print('%s is running' % name)
    time.sleep(3)
    print('%s is done' % name)
    p.start()
    


if __name__ == '__main__':
    p = Process(target=task, args=('alex',))
    # 开启守护进程
    p.daemon = True
    p.start()
    time.sleep(5)
    print('主')
