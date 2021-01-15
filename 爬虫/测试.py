from concurrent.futures import ThreadPoolExecutor
import requests
import time


def get(url):
    print(url)
    return url


def parse(x):
    print (x)


if __name__ == "__main__":
    pool = ThreadPoolExecutor(5)
    urls = [
        'https://www.baidu.com',
        'https://www.baidu.com',
    ]

    for url in urls:
        # 把submit执行后的obj，给parse
        obj=pool.submit(get, url)
        print(obj.result())
        # .add_done_callback(parse)
