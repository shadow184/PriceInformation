import logging

def ItemContainsNull(item):
	for s in ['itemType', 'price', 'date', 'quantity', 'store', 'name']:
		if item[1][s] is None:
			logging.warning("Property is null, not inserting.")
			return True
	return False