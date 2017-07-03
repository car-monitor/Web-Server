from pymongo import MongoClient
from bson.objectid import ObjectId
import config


class Unit:
	def __init__(self, client):
		#client = MongoClient(config.address, config.port)
		self.db = client[config.dbname]
		self.unit_collection = self.db.unit_collection

	def create(self, data):
		unitId = self.unit_collection.insert({'name': data['name']})
		data['id'] = unitId
		return data

	def retrieve(self, data):
		if data.has_key('id'):
			unit = self.unit_collection.find({'_id': ObjectId(data['id'])})
			unit['id'] = str(unit['_id'])
			del unit['_id']
			return unit
		else:
			units = self.unit_collection.find()
			for unit in units:
				unit['id'] = str(unit['_id'])
				del unit['_id']
			return units