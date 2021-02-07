from gevent import joinall, spawn, monkey
monkey.patch_all()
from threading import Thread, current_thread
import requests


def parse_page(res):
    # res = res.result()
    print('%s PARSE %s' % (current_thread().  getName(), len(res)))


def get_page(url, callback=parse_page):
    print('%s GET %s' % (current_thread().getName(), url))
    response = requests.get(url)
    if response.status_code == 200:
        callback(response.text)


if __name__ == '__main__':
    urls = [
        'https://www.baidu.com',
        'https://www.taobao.com',
        'https://www.hao123.com'

    ]

    tasks = []
    for url in urls:
        tasks.append(spawn(get_page, url))
    joinall(tasks)


