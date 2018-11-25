from PriceInformation.items import PriceinformationItem
from datetime import datetime

def danMurphysParser(response):
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
            
	return d