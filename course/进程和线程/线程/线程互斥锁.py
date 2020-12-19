from threading import Thread
n=100
import time
def task():
    global n
    temp=n
    time.sleep(0.1)
    n=temp-1 

if __name__ == "__main__":
    t_l=[]
    for i in range(100):
        t=Thread(target=task)
        t.start()
    for t in t_l:
        t.join()
    print('主')