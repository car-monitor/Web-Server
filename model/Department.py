from pymongo import MongoClient
from bson.objectid import ObjectId
import config


class Department:
	def __init__(self, db):
		self.department_collection = db.department_collection

	def create(self, data):
		departmentId = self.department_collection.insert(data)
		data['id'] = str(departmentId)
		del data['_id']
		return data

	def retrieve(self, data = {}):
		if data.has_key('id'):
			data['_id'] = ObjectId(data['id'])
			del data['id']
			
		if data != {}:
			department = self.department_collection.find_one(data)
			if department != None:
				department['id'] = str(department['_id'])
				del department['_id']
				return department
		else:
			cursor = self.department_collection.find()
			departments = []
			for department in cursor:
				department['id'] = str(department['_id'])
				del department['_id']
				departments.append(department)
			return departments
