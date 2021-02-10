# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider,CrawlSpider,XMLFeedSpider,CSVFeedSpider,SitemapSpider

class AmazonSpider(scrapy.Spider): #自定义类，继承Spiders提供的基类
    name = 'amazon'
    allowed_domains = ['www.amazon.cn']
    start_urls = ['http://www.amazon.cn/']
    

def parse(self, response):
    pass
