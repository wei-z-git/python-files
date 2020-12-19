from threading import Thread
import time


def sayhi(name):
    time.sleep(2)
    print('%s say hello' % name)


if __name__ == '__main__':
    t = Thread(target=sayhi, args=('egon',))
    # t.daemon=True  开启后主线程不等守护线程，直接跑完就完了
    t.start()
    # 默认主线程会等待子线程
    print('主线程')
 

