from pymongo import MongoClient
from bson.objectid import ObjectId
import config


class Unit:
	def __init__(self, db):
		self.unit_collection = db.unit_collection

	def create(self, data):
		unitId = self.unit_collection.insert(data)
		data['id'] = str(unitId)
		del data['_id']
		return data

	def retrieve(self, data = {}):
		if data.has_key('id'):
			data['_id'] = ObjectId(data['id'])
			del data['id']
		if data != {}:
			unit = self.unit_collection.find_one(data)
			if unit != None:
				unit['id'] = str(unit['_id'])
				del unit['_id']
			return unit
		else:
			data = self.unit_collection.find()
			units = []
			for unit in data:
				unit['id'] = str(unit['_id'])
				del unit['_id']
				units.append(unit)
			return units
