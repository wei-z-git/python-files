import requests
import re
import hashlib
import time
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(50)
movie_path = r"D:\haha"


def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except Exception:
        pass


def parse_index(index_page):
    index_page = index_page.result()
    urls = re.findall('class="c_b_p_desc".*?href="(.*?)"', index_page, re.S)
    print(urls)
    for url in urls:
        detail_url = url
        pool.submit(get_page, detail_url).add_done_callback(parse_detail)
        # 很奇怪，这里会非调试会显示解释器已关闭


def parse_detail(detail_page):
    detail_page = detail_page.result()
    movie_url = re.findall(
        'class="postTitle2 vertical-middle".*?href="(.*?)"', detail_page, re.S)
    if movie_url:
        movie_url = movie_url[0]  # 剔除空列表
        if movie_url.endswith('html'):
            # pool.submit(get_movie, movie_url)
            pass


def get_movie(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            m = hashlib.md5()
            m.update(str(time.time()).encode('utf-8'))
            m.update(url.encode('utf-8'))
            filepath = r'%s\%s.mp4' % (movie_path, m.hexdigest())
            with open(filepath, 'wb') as f:
                f.write(response.content)
                print('%s 下载成功' % url)
    except Exception:
        pass


# def main():



if __name__ == "__main__":
    base_url = 'https://www.cnblogs.com/xiaoyuanqujing/'
    for i in range(1):
        url = base_url.format(page_num=i)
        # 线程异步提交任务，不去等待结果，完成后直接调用parse_index
        pool.submit(get_page, url).add_done_callback(parse_index)
