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
		if self.collection != None:
			Name = warningDict_information['name']
			Detail = warningDict_information['detail']
			self.collection.insert({'name': Name, 'detail': Detail})
			#rs = self.collection.find_one({'name':Name})
			return{'status': 1}  # return {'status': 1, 'warningDict':rs}  used to test
		else:
			return {'status': 0}

	def retrieve(self):
		rs = self.collection.find()

		if rs != None:
			for items in rs:
				items['id'] = str(items['_id'])
				del items['_id']
			return {'status': 1, 'warnings':rs}
		else:
			return {'status': 0}

	def retrieve(self, string_id):
		rs = self.collection.find_one({'_id':ObjectId(string_id['id'])})

		if rs != None:
			rs['id'] = str(rs['_id'])
			del rs['_id']
			return {'status': 1, 'warnings': rs}
		else:
			return {'status': 0}

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