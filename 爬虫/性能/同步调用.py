import requests
from threading import Thread, current_thread
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def parse_page(res):
    res = res.result()
    print('%s PARSE %s' % (current_thread().getName(), len(res)))


def get_page(url):
    print('%s GET %s' % (current_thread().getName(), url))
    response = requests.get(url)
    if response.status_code == 200:
        return response.text


if __name__ == '__main__':
    urls = [
        'https://www.baidu.com',
        'https://www.taobao.com',
        'https://www.hao123.com'

    ]

    pool = ThreadPoolExecutor(50)
    for url in urls:
        pool.submit(get_page, url).add_done_callback(parse_page)

    pool.shutdown(wait=True)
