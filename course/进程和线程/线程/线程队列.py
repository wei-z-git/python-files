import queue

q=queue.Queue()
q.put('first')
q.put('second')
q.put('third')

print(q.get())
print(q.get())
print(q.get())
'''
结果(先进先出):
first
second
third
'''