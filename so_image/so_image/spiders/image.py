# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json


class ImageSpider(scrapy.Spider):
    name = 'image'
    BASE_URL = 'http://image.so.com/zj?ch=art&sn=%s&listtpye=new&temp=1'
    start_index = 0
    MAX_DOWNLOAD = 500
    start_urls = [BASE_URL%0]

    def parse(self, response):
        infos = json.loads(response.body.decode('utf8'))
        yield{
            'image_urls': [info['qhimg_url'] for info in infos['list']]
        }
        self.start_index += infos['count']
        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD:
            yield Request(self.BASE_URL%self.start_index)
