import time
import random
from multiprocessing import Process,Queue

def producer(name, food,q):
    for i in range(1, 10):
        res = '%s%s' % (food,i)
        time.sleep(random.randint(1, 3))
        q.put(res)
        print('厨师[%s]生产了<%s>' %(name,res))



def consumer(name, q):
    while True:
        res=q.get()
        time.sleep(random.randint(1, 3))
        print('吃货[%s]吃了<%s>' % (name, res))


if __name__=='__main__':
    # 队列
    q=Queue()
    # 生产者们
    p1=Process(target=producer,args=('tom','泔水',q))

    # 消费者
    c1=Process(target=consumer,args=('jerry',q))
    p1.start()
    c1.start()
    print('主')