import requests
import re
import hashlib
import time


movie_path = r"D:\code\python-files\爬虫\download"


def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except Exception:
        pass



def parse_index(index_page):
    # re.S参数以后，正则表达式会将这个字符串作
    # 为一个整体，将“\n”当做一个普通的字符加入到这个字符串中
    urls = re.findall('class="c_b_p_desc".*?href="(.*?)"', index_page, re.S)
    for url in urls:
        if not url.startswith('https'):
            url = 'https://www.cnblogs.com/xiaoyuanqujing'+url
        yield url


def parse_detail(detail_page):
    movie_url = re.findall(
        'class="postTitle2 vertical-middle".*?href="(.*?)"', detail_page, re.S)
    if movie_url:
        movie_url = movie_url[0]  # 剔除空列表
        if movie_url.endswith('html'):
            yield movie_url
    # 迭代器，输出


def get_movie(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            m = hashlib.md5()
            m.update(str(time.time()).encode('utf-8'))
            m.update(url.encode('utf-8'))
            filepath = '%s\%s.mp4' % (movie_path, m.hexdigest())
            with open(filepath, 'wb') as f:
                f.write(response.content)
                print('%s 下载成功'%url)
    except Exception:
        pass



def main():
    base_url = 'https://www.cnblogs.com/xiaoyuanqujing/'
    # base_url = 'https://www.cnblogs.com/xiaoyuanqujing/list-{page_num}.html'
    # .format格式化函数{},url=base_url.format(page_num=i)
    for i in range(1):
        url = base_url.format(page_num=i)
        index_page = get_page(url)
        detail_urls = parse_index(index_page)
        for detail_url in detail_urls:
            detail_page = get_page(detail_url)
            movie_urls = parse_detail(detail_page)
            for movie_url in movie_urls:
                get_movie(movie_url)


if __name__ == "__main__":
    main()
