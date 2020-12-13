from multiprocessing import Process,Lock
import json
import time
import random
import os


def search():
    time.sleep(random.randint(1, 3))
    dic = json.load(
        open('db.txt', "r", encoding='utf-8'))
    print('%s查看到剩余票%s' % (os.getpid(), dic['count']))


def get():
    dic = json.load(
        open('db.txt', "r", encoding='utf-8'))
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(random.randint(1, 3))
        json.dump(dic, open('db.txt', "w", encoding='utf-8'))
        print('%s购票成功' % os.getpid())


def task(mutex):
    # 3、给进程加锁,只给购买操作加锁
    search()
    mutex.acquire()
    get()
    mutex.release()


if __name__ == '__main__':
    # 1、实例化一个互斥锁
    mutex=Lock()
    for i in range(10):
        # 2、锁传给子进程
        p = Process(target=task,args=(mutex,))
        p.start()

