from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import random
import os


def task(n):
    print('%s is runnning' % os.getpid())
    time.sleep(random.randint(1, 3))
    return n**2


if __name__ == "__main__":
    # 指定池的大小 ，进程池不要超过cpu*2
    pool = ProcessPoolExecutor(2)
    for i in range(5):
        # 提交到进程池，异步提交，接了5客人，俩人运行
        pool.submit(task, i)
    # 等待进程池所有进程都运行完毕，  源码：相当于是每个进程调用了join
    pool.shutdown(wait=True)
    print('主')
