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

#超时设置
#两种超时:float or tuple
#timeout=0.1 #代表接收数据的超时时间
#timeout=(0.1,0.2)#0.1代表链接超时  0.2代表接收数据的超时时间

import requests
respone=requests.get('https://www.baidu.com',
                     timeout=0.0001)