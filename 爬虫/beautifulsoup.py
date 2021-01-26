from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#基本使用：容错处理,文档的容错能力指的是在html代码不完整的情况下,使用该模块可以识别该错误。使用BeautifulSoup解析上述代码,能够得到一个 BeautifulSoup 的对象,并能按照标准的缩进格式的结构输出
from bs4 import BeautifulSoup
soup=BeautifulSoup(html_doc,'lxml') 
res=soup.prettify() #处理好缩进，结构化显示

# print(soup.a.text) 
# print(soup.a.attrs) #字典

# print(soup.p.contents)# p的子节点
# print(soup.p.children) #生成器

# 搜索文档数五种过滤器

# 1、字符串

# print(soup.find_all(name='a'))
# print(soup.find_all(attrs={"class":"sister"}))
print(soup.find_all(name='b',text='The ')