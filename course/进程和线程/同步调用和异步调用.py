# 提交任务的两种方式：
# 同步调用：提交完任务后，就在原地等待，等待任务执行完毕，拿到任务返回值，
#   才能继续下一行代码，导致程序串行执行
# 异步调用+回调机制：提交完任务后，不在原地等待，任务一旦执行完毕就会触发回调函数的执行，导致程序并发执行


# 阻塞
# 非阻塞

# # 同步调用实例
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
# import time
# import random
# import os


# def task(n):
#     print('%s is runnning' % os.getpid())
#     time.sleep(random.randint(1, 3))
#     return n**2


# # 处理结果的函数
# def handle(res):
#     print('handle res %s' % res)


# if __name__ == "__main__":
#     pool = ProcessPoolExecutor(2)
#     for i in range(5):
#         # 提交到进程池，异步提交,但是加了.result()后，
#         # 相当于是要去拿结果，程序就会串着执行，所以这样也方便了后续有调用task()的函数，直接拿到task()的结果
#         res = pool.submit(task, i).result()
#         print('res is %s' % res)
#         # handle(res)
#     # 等待进程池所有进程都运行完毕，join
#     pool.shutdown(wait=True)
#     print('主')


# 异步调用实例
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import random
import os


def task(n):
    print('%s is runnning' % os.getpid())
    time.sleep(random.randint(1, 3))
    return n**2



# 处理结果的函数
def handle(res):
    # 3、handle拿到obj，然后拿到他的结果
    res=res.result()
    print('handle res %s' % res)


if __name__ == "__main__":
    pool = ProcessPoolExecutor(2)
    for i in range(5):
        #1、 某个任务完成后，立马触发一个回调函数，调用handle方法
        #2、 本来obj可以直接通过result直接拿结果，现在一旦task运行结束了 2、立马触发回调函数，把obj传给handle
        obj = pool.submit(task, i)
        obj.add_done_callback(handle)

    pool.shutdown(wait=True)
    print('主')