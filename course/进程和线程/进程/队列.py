from multiprocessing import Queue
# 先进先出
# 队列里不能放大数据
# 队列占用内存
q=Queue(3)
q.put('first')
q.put(2)
q.put({'count':3})

#  只能放仨，再放锁就阻塞住了，除非取走
# 1、默认阻塞，block=False后不阻塞(直接报错)   
# 2、相当于q.put_nowait('fourth')  
# 3、以及timeout
# q.put('fourth',block=False，timeout=3)


print(q.get())
print(q.get())
print(q.get())
