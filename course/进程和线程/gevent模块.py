import gevent
from gevent import monkey
import time
# 打补丁，发现是io型则切
monkey.patch_all()


def eat(name):
    print('%s eat1' % name)
    # gevent.sleep(1)
    time.sleep(2)
    print('%s eat2' % name)


def play(name):
    print('%s play1' % name)
    # gevent.sleep(2)
    time.sleep(1)
    print('%s play2' % name)

# 实例两个协程对象
a=time.time()
g1 = gevent.spawn(eat, 'egon')
g2 = gevent.spawn(play, 'alex')


# 等待所有协程都结束后再结束主进程
gevent.joinall([g1,g2])
b=time.time()
print(b-a)