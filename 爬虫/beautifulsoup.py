from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="sister"><b>The Dormouse's story</b></p>
<p class="title" id=1><b>$37</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# 基本使用：容错处理,文档的容错能力指的是在html代码不完整的情况下,使用该模块可以识别该错误。使用BeautifulSoup解析上述代码,能够得到一个 BeautifulSoup 的对象,并能按照标准的缩进格式的结构输出
soup = BeautifulSoup(html_doc, 'lxml')
res = soup.prettify()  # 处理好缩进，结构化显示

# print(soup.a.text)
# print(soup.a.attrs) #字典

# print(soup.p.contents)# p的子节点
# print(soup.p.children) #生成器

# 搜索文档数五种过滤器

# 1、字符串
# 根据名称
# print(soup.find_all(name='a'))
# 根据属性
# print(soup.find_all(attrs={"class":"sister"}))
# soup.find_all()
# print(soup.p.find_all(name='b'))
# print(soup.find(name='p',attrs={'class':'story'}).find_all(name='a')[0])

# 2、正则
# print(soup.find_all(name=re.compile('^b')))

# print(soup.find_all(attrs={'id':re.compile('link')}))
# print(soup.find_all(text=re.compile('\$')))

#3、 列表(或的意思，满足列表中一个条件即可)，和# print(soup.find(name='p',attrs={'class':'story'}).find_all(name='a')[0])
# 相对
# print(soup.find_all(name=['a',re.compile('b')]))

# 4、true
# 查找标签有name字段的，  查找标签有id字段的
# print(soup.find_all(name=True))
# print(soup.find_all(attrs={"id":True}))
# 找到标签名p，有id属性的标签
# print(soup.find_all(name='p',attrs={"id":True}))

# 其他
# 限制数目
# print(soup.find_all(name='p',limit=2))
# 没看懂???，不迭代么这是
# print(soup.body.find_all(attrs={"class":"sister"},recursive=False))

# print(soup.find_all(class_="sister"))
