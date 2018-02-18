# -*- coding: utf-8 -*-
import scrapy
import requests
import re
import time

from CygSpider.items import PetItem
from scrapy.http import Request #用于parse中，访问url并执行回调函数
from selenium import webdriver #selenium构造浏览器访问实例用
from scrapy.selector import Selector #将使用selenium获取的页面内容包成一个selector,使用selector里的css选择器或者xpath选择器效率比selenium的高
from urllib import parse #之后链接url地址用

class CygSpider(scrapy.Spider):
    name = 'cyg'
    allowed_domains = ['cyg.changyou.com']
    start_urls = ['http://cyg.changyou.com/details/?goodsCode=1621801291912220231']

    agent = "Mozilla / 5.0(X11;Ubuntu;Linuxx86_64;rv: 56.0) Gecko / 20100101Firefox / 56.0"
    header = {
        "HOST" : "cyg.changyou.com",
        "Referer" : "http://cyg.changyou.com",
        "User-Agent" : agent,
    }

    page_num = 5
    cur_page_num = 3
    urls = []
    browser = webdriver.Firefox(executable_path = "/usr/local/bin/geckodriver")

    def start_requests(self):
        new_urls = self.collect_urls()
        self.urls = new_urls
        return [Request('http://cyg.changyou.com/details/?goodsCode=1621801291912220231', callback=self.parse, headers=self.header)]

    def parse(self, response):
        for url in self.urls:
            cur_url = parse.urljoin(response.url, url)
            time.sleep(1)
            yield Request(url = cur_url, callback=self.parse_detail, headers=self.header)


        urls = self.collect_urls()
        if urls:
            yield Request('http://cyg.changyou.com',callback=self.parse)


    def parse_detail(self, response):
        pet_item = PetItem()
        name = response.css(".goodsname::text").extract()[0]
        price = response.css(".m-money-points::text").extract()[0].strip()
        pet_item["name"] = name
        pet_item["price"] = price
        yield pet_item  #item被yield后传入pipelines，记得在setting中启用pipeline

    def collect_urls(self):
        if(self.cur_page_num > self.page_num): return []
        self.browser.get("http://cyg.changyou.com/list#!gameId=16&sort=price,asc&area=%E7%94%B5%E4%BF%A1%E4%B8%80%E5%8C%BA,%E7%94%B5%E4%BF%A1%E4%B8%80%E5%8C%BA&server=104,%E4%BE%A0%E5%AE%A2%E5%B2%9B,1004&goodsType=4")
        time.sleep(20)
        self.browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[3]/div[2]/div/a[{}]/span".format(self.cur_page_num)).click()
        self.cur_page_num += 1
        time.sleep(20)
        page_content = self.browser.page_source
        selector = Selector(text = page_content)

        res = selector.css("li.item > div > div > h2 > a::attr(href)").extract()
        return res