import pymongo
import config 

from pymongo import MongoClient
from bson.objectid import ObjectId

class WarningDict:
	def __init__(self, client):
		#client = MongoClient(config.address, config.port)
		self.db = client[config.dbname]
		self.collection = self.db.warningDict_collection

	def create(self, warningDict_information):
		if self.connection != None:
			Name = warningDict_information['name']
			Detail = warningDict_information['detail']
			self.collection.insert({'name': Name, 'detail': Detail})
			return {'status': 1}
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

	def retrieve(self):
		rs = self.collection.find()

		if rs != None:
			for items in rs:
				items['id'] = str(items['_id'])
				del items['_id']
			return {'status': 1, 'warnings':rs}
		else:
			return {'status': 0}

