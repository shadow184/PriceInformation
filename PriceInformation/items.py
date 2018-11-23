import scrapy

class PriceinformationItem(scrapy.Item):
	name = scrapy.Field()
	price = scrapy.Field()
	quantity = scrapy.Field()
	store = scrapy.Field()
	date = scrapy.Field()
