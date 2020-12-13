import time
import random
from multiprocessing import Process, JoinableQueue


def producer(name, food, q):
    for i in range(3):
        res = '%s%s' % (food, i)
        time.sleep(random.randint(1, 3))
        q.put(res)
        print('厨师[%s]生产了<%s>' % (name, res))


def consumer(name, q):
    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print('吃货[%s]吃了<%s>' % (name, res))
        # 2、调用task_done()，每次q.get()后告诉q.join()队列少一个
        q.task_done()


if __name__ == '__main__':
    # 队列
    q = JoinableQueue()
    q.task_done
    # 生产者们
    p1 = Process(target=producer, args=('tom', '泔水', q))
    p2 = Process(target=producer, args=('tom2', '骨头', q))
    # 消费者
    c1 = Process(target=consumer, args=('jerry', q))
    c2 = Process(target=consumer, args=('jerry2', q))
    c3 = Process(target=consumer, args=('jerry3', q))
    # 3、c1，c2，c3设为守护进程，因为等主进程运行完了，说明队列里已经没消息了，所以c1、c2、c3没有存在意义了
    c1.daemon=True
    c2.daemon=True
    c3.daemon=True

    p1.start()
    p2.start()

    c1.start()
    c2.start()
    c3.start()
    p1.join()
    p2.join()
    # 1、等待队列结束，此时生产者已经不再向队列放消息，剩余的每个消费者
    q.join()

    print('主')
