from threading import Event,Thread,current_thread
# 如果某线程的任务的执行得先等另一个线程的任务执行完，那么需要用event来设置当前线程任务的状态
e=Event()

def check_mysql():
    print('正则检测mysql',e.is_set())
    import time
    time.sleep(2)
    e.set()

def conn_mysql():
    count=0
    while count < 3:
        print('<%s>第%s次尝试链接' % (current_thread().getName(), count))
        e.wait(0.5)
        if e.is_set():
            print('<%s> 链接成功' % current_thread().getName())
            break
        count+=1
    else:
        # raise TimeoutError("链接超时")
        print("<%s> 链接超时" % current_thread().getName())

if __name__ == '__main__':
    t1=Thread(target=check_mysql)
    t2=Thread(target=conn_mysql)
    t1.start()
    t2.start()
