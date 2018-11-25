# -*- coding: utf-8 -*-
import scrapy
from danMurphysParser import danMurphysParser

class DanMurphysBeerSpider(scrapy.Spider):
    name = 'dan-murphys'

    def start_requests(self):
		url = 'https://www.danmurphys.com.au/current-offers?filters=variety(beer)&size=120'

		yield scrapy.Request(url, self.parse, meta={
			'splash': {
				'endpoint': 'render.html',
				'args': { 'wait': 0.5 }
			}
		})

    def parse(self, response):
        yield danMurphysParser(response)