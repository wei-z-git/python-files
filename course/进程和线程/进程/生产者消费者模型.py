import time
import random
from multiprocessing import Process,Queue

def producer(name, food,q):
    for i in range(3):
        res = '%s%s' % (food,i)
        time.sleep(random.randint(1, 3))
        q.put(res)
        print('厨师[%s]生产了<%s>' %(name,res))



def consumer(name, q):
    while True:
        res=q.get()
        # 判断，如果是None，则退出循环
        if res==None:
            break
        time.sleep(random.randint(1, 3))
        print('吃货[%s]吃了<%s>' % (name, res))


if __name__=='__main__':
    # 队列
    q=Queue()
    # 生产者们
    p1=Process(target=producer,args=('tom','泔水',q))
    p2=Process(target=producer,args=('tom2','骨头',q))
    # 消费者
    c1=Process(target=consumer,args=('jerry',q))
    c2=Process(target=consumer,args=('jerry2',q))
    c3=Process(target=consumer,args=('jerry3',q))

    p1.start()
    p2.start()


    c1.start()
    c2.start()
    c3.start()
    # 主进程等待生产者进程生产完
    p1.join()
    p2.join()
    # 队列里放入None值
    q.put(None)
    q.put(None)
    q.put(None)
    print('主')