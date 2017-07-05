from pymongo import MongoClient
from bson.objectid import ObjectId
import config


class Department:
	def __init__(self, client):
		#client = MongoClient(config.address, config.port)
		self.db = client[config.dbname]
		self.department_collection = self.db.department_collection

	def create(self, data):
		departmentId = self.department_collection.insert({'name': data['name']})
		data['id'] = departmentId
		return data

	def retrieve(self, data):
		if data.has_key('id'):
			department = self.department_collection.find({'_id': ObjectId(data['id'])})
			department['id'] = str(department['_id'])
			del department['_id']
			return department
		else:
			departments = self.department_collection.find()
			for department in departments:
				department['id'] = str(department['_id'])
				del department['_id']
			return departments