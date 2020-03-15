# import time


# def index():
#     time.sleep(3)
#     print("welcome to index")


# def timmer(func):
#     start = time.time()
#     func()
#     stop = time.time()
#     print("run time is %s" % (stop-start))

# timmer(index)

import time


def timmer(func):
    # func = index
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print("run time is %s" % (stop-start))
        return res
    return inner


@timmer
def index(name):
    print("welcome %s to index" % name)
    return 1111


index("haha")
