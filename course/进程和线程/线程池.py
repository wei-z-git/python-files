from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
import requests
import time


def get(url):
    print('%s get %s' % (current_thread().getName(), url))
    response = requests.get(url)
    time.sleep(2)
    if response.status_code == 200:
        return {'url': url, 'content': response.text}


def parse(res):
    res = res.result()
    print('parse [%s] res: [%s]' % (res['url'], len(res['content'])))


if __name__ == "__main__":
    pool = ThreadPoolExecutor(5)
    urls = [
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.openstack.org',
        'https://www.openstack.org',
        'https://www.openstack.org',
        'https://www.openstack.org',
        'https://www.openstack.org',
        'https://www.openstack.org',
        'https://www.openstack.org',
        'https://www.openstack.org',
    ]

    for url in urls:
        pool.submit(get, url).add_done_callback(parse)
