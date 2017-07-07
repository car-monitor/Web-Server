import pymongo
import config 

from pymongo import MongoClient
from bson.objectid import ObjectId

class WarningDict:
	def __init__(self, client):
		#self.client = MongoClient(config.address, 27017)
		self.db = client[config.dbname]
		self.collection = self.db.warningDict_collection

	def create(self, warningDict_information):
		warningdictid = self.collection.insert(warningDict_information)
		warningDict_information['id'] = str(warningdictid)
		del warningDict_information['_id']
		return warningdictid

	def retrieve(self, data={}):
		if data.has_key('id'):
			data['_id'] = ObjectId(data['id'])
			del data['id']

		if data != {}:
			rs = self.collection.find_one({'_id':data['id']})
				if rs != None:
					rs['id'] = str(rs['_id'])
					del rs['_id']
					return rs
				else:
					return
		else:
			Dicts = []
			dicts = self.collection.find()
			for item in dicts:
				item['id'] = str(items['_id'])
				del item['_id']
				Dicts.append(item)
			return Dicts

'''
test case:

if __name__ == '__main__':
	WarnDict = WarningDict()
	dict = {'name':'Kristen_Stewart',
			'detail':'She is a very good actress -- The Godness of Kwight!'
			}
	result = WarnDict.create(dict)
	if result['status'] == 1:
		print WarnDict.retrieve({'id':result['warningDict']['_id']})
'''