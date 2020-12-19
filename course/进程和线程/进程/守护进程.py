from multiprocessing import Process
import time


def task(name):
    print('%s is running' % name)
    time.sleep(3)
    print('%s is done' % name)
    


if __name__ == '__main__':
    p = Process(target=task, args=('alex',))
    # 开启守护进程
    # p.daemon = True  开启后主进程不等守护进程，直接跑完就完了
    p.start()
    print('主')
