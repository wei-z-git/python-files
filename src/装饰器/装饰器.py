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
    def inner():
        start = time.time()
        func()
        stop = time.time()
        print("run time is %s" % (stop-start))
    return inner


@timmer
def index():
    time.sleep(3)
    print("welcome to index")


index()
