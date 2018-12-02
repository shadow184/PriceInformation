import logging
import MySQLdb
from common import ItemContainsNull

class MySqlPipeline(object):
	def __init__(self):
		self.conn = MySQLdb.connect('IP', 'USERNAME', 'PASSWORD', 'TABLENAME', charset="utf8", use_unicode=True)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		for i in item.iteritems():
			if not ItemContainsNull(i):
				self.cursor.execute("""INSERT INTO Product (Type, Price, Date, Quantity, Store, Name)  
							VALUES (%s, %s, %s, %s, %s, %s)""", 
						   (i[1]['itemType'], 
							i[1]['price'],
							i[1]['date'],
							i[1]['quantity'],
							i[1]['store'],
							i[1]['name']))
				self.conn.commit()