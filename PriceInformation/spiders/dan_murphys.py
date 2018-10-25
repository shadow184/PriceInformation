# -*- coding: utf-8 -*-
import scrapy


class DanMurphysBeerSpider(scrapy.Spider):
    name = 'dan-murphys'

    def start_requests(self):
        yield scrapy.Request('https://www.danmurphys.com.au/current-offers?filters=variety(beer)&size=120', self.parse, meta={
            'splash': {
                'endpoint': 'render.html',
                'args': { 'wait': 0.5 }
            }
        })

    def parse(self, response):
        for p in response.css('.product-content'):
            product = p.css('.title::text').extract_first()
            yield {
                    'product': product,
                    'price': p.css('.value::text').extract(),
                    'quantity': p.css('.quantity::text').extract()
            }