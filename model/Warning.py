import pymongo
import config 

from pymongo import MongoClient
from bson.objectid import ObjectId

class Warning:
	def __init__(self, client):
		#self.client = MongoClient(config.address, 27017)
		self.db = client[config.dbname]
		self.collection = self.db.warning_collection

	def create(self, warning_Information):
		warningid = self.collection.insert(warning_Information)
		warning_Information['id'] = str(warningid)
		del warning_Information['_id']
		return warning_Information

''' 
decide by the key that input -- 'id' OR 'userId'
which 'id' means the recordId in the database,
and 'userId' means the dirverId
'''
	def retrieve(self, data):
		if data.has_key('id'):
			data['waybillID'] = data['id']
			del data['id']

		Dict = []
		result = self.collection.find({'waybillID':data['waybillID']})
		if result != None:
			for item in result:
				item['id'] = str(item['_id'])
				del item['_id']
				Dict.append(item)
			return Dict


'''
test case:

if __name__ == '__main__':
	warn = Warning()
	dict = {'startID':2312, 'endID':2345, 'type':'Overspeed',
			'status':0, 'waybillID':46878779
			}
	result = warn.create(dict)
	if result['status'] == 1:
		print warn.retrieve({'id':result['warning']['_id']})
'''