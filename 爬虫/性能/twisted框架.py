from 爬虫.性能.检测io自动切换 import parse_page
from twisted.web.client import defer, getPage
from twisted.internet import reactor


def parse(res):
    pass


def all_done(res):
    print(res)
    reactor.stop()


urls = [
    'https://www.baidu.com',
    'https://www.taobao.com',
    'https://www.hao123.com'

]

tasks = []
for i in urls:
    obj = getPage(url)
    obj.addCallback(parse_page)
    tasks.append(obj)
defer.DeferredList(tasks).addBoth(all_done)
reactor.run()
