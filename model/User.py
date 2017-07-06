from pymongo import MongoClient
from bson.objectid import ObjectId
import config


class User:
	def __init__(self, db):
		self.user_collection = db.user_collection

	def create(self, data):
		self.user_collection.insert({'username': data['username'], 'password': data['password']})

	def retrieve(self, data):
		if data.has_key('id'): 
			data['_id'] = ObjectId(data['id'])
			del data['id']
		
		cursor = self.user_collection.find(data)
		users = []
		for user in cursor:
			user['id'] = str(user['_id'])
			del user['_id']
			users.append(user)
		
		if len(users) == 0:
			return None
		else if len(users) == 1:
			return users[0]
		else:
			return users

	def update(self, data):
		user = self.user_collection.find_one({'_id': ObjectId(data['id'])})
		if user != None:
			for key in data:
				if key != 'id': user[key] = data[key]
			self.user_collection.save(user)
			if not data.has_key('authority'):
				user['id'] = str(user['_id'])
				del user['_id']
				return user
