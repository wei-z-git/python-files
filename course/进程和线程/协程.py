'''
单纯地切换反而会降低运行效率

'''

# # 串行执行
# import time


# def consumer(res):
#     pass


# def producer():
#     res = []
#     for i in range(10000000):
#         res.append(i)
#     return res


# start = time.time()
# res = producer()
# consumer(res)
# stop = time.time()
# print(stop - start)


#基于yield并发执行
import time
def consumer():
    while True:
        yield

def producer():
    g=consumer()
    next(g)
    for i in range(10000000):
        g.send(i)

start=time.time()
producer()
stop=time.time()
print(stop-start)
