# -*- coding: utf-8 -*-
import scrapy
from PriceInformation.items import PriceinformationItem
from datetime import datetime


class DanMurphysBeerSpider(scrapy.Spider):
    name = 'dan-murphys'

    def start_requests(self):
		urls = ['https://www.danmurphys.com.au/current-offers?filters=variety(beer)&size=120']
		for u in urls:
			yield scrapy.Request(u, self.parse, meta={
				'splash': {
					'endpoint': 'render.html',
					'args': { 'wait': 0.5 }
				}
			})

    def parse(self, response):
        productList = []

        for p in response.css('.product-content'):
			product = PriceinformationItem()

			pro = p.css('.title::text').extract_first()
            
			for pr in p.css('.value'):
				product['name'] = pro
				product['price'] = pr.css('.value::text').extract_first()
            
			for q in p.css('.quantity'):
				product['quantity'] = q.css('.quantity::text').extract_first()

			# substring the response url for the item type E.G: Beer, Spirits
			product['itemType'] = str(response)[str(response).index('(') + 1:str(response).index(')')]
			product['store'] = 'Dan Murphys'
			product['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			productList.append(product)

        d = {str(i) : productList[i] for i in range(0, len(productList))}
            
        yield d