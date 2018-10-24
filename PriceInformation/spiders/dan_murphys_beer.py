# -*- coding: utf-8 -*-
import scrapy


class DanMurphysBeerSpider(scrapy.Spider):
    name = 'dan-murphys-beer'

    def start_requests(self):
        yield scrapy.Request('https://www.danmurphys.com.au/current-offers?filters=variety(beer)', self.parse, meta={
            'splash': {
                'endpoint': 'render.html',
                'args': { 'wait': 0.5 }
            }
        })

    def parse(self, response):
        for p in response.css('.product-content'):
            yield {
                    'product': p.css('.title::text').extract(),
                    'price': p.css('.value::text').extract(),
                    'quantity': p.css('.quantity::text').extract()
            }