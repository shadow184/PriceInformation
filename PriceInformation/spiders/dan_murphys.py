# -*- coding: utf-8 -*-
import scrapy
from danMurphysParser import danMurphysParser
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

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

class DanMurphysSpiritsSpider(scrapy.Spider):
	name = 'dan-murphys-spirits'
	def start_requests(self):
		url = 'https://www.danmurphys.com.au/current-offers?filters=variety(spirits)&size=120'

		yield scrapy.Request(url, self.parse, meta={
			'splash': {
				'endpoint': 'render.html',
				'args': { 'wait': 0.5}
			}
		})

	def parse(self, response):
		yield danMurphysParser(response)

class DanMurphysRedWineSpider(scrapy.Spider):
	name = 'dan-murphys-red-wine'
	def start_requests(self):
		url = 'https://www.danmurphys.com.au/current-offers?filters=variety(red-wine)&size=120'

		yield scrapy.Request(url, self.parse, meta={
			'splash': {
				'endpoint': 'render.html',
				'args': { 'wait': 0.5}
			}
		})

	def parse(self, response):
		yield danMurphysParser(response)

process = CrawlerProcess(get_project_settings())
process.crawl(DanMurphysBeerSpider)
#process.crawl(DanMurphysSpiritsSpider)
#process.crawl(DanMurphysRedWineSpider)
process.start()