# -*- coding: utf-8 -*-
'''
问题一：图片文件夹没有找到，下载成功了，mongodb中也有信息，应该是图片存储方式没搞懂
问题二：为什么在images.py文件要导入item.py的包，应该scrapy自动调用才对
'''
import scrapy
from scrapy import Spider, Request
from urllib.parse import urlencode
import json
from images360.items import Images360Item

class ImagesSpider(scrapy.Spider):

    name = 'images'
    allowed_domains = ['images.so.com']
    def start_requests(self):
        data_url = {'ch': 'beauty','listtype': 'new'}
        base_url = 'http://image.so.com/zj?'
        for page in range(1, 51):
            data_url['sn'] = page * 30
            params = urlencode(data_url)
            url = base_url + params
            yield Request(url, self.parse)
    def parse(self, response):
        result = json.loads(response.text)
        p = result.get('list')
        #print(p)
        if p is not None:
            for image in p:
                item = Images360Item()
                item['id'] = image.get('imageid')
                item['url'] = image.get('qhimg_url')
                item['title'] = image.get('group_title')
                item['thumb'] = image.get('qhimg_thumb_url')
                yield item
