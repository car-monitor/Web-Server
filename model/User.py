from pymongo import MongoClient
from bson.objectid import ObjectId
import config


class User:
	def __init__(self, client):
		#client = MongoClient(config.address, config.port)
		self.db = client[config.dbname]
		self.user_collection = self.db.user_collection

	def create(self, data):
		result = self.user_collection.find_one({'username': data['username']})
		self.user_collection.insert({'username': data['username'], 'password': data['password']})

	def retrieve(self, data):
		#ignore the function of keyword
		if data.has_key('authority'): 
			users = self.user_collection.find({'authority': data['authority']})
			for user in users:
				user['id'] = str(user['_id'])
				del user['_id']
			return users
		else: 
			user = self.user_collection.find_one({'username': data['username']})
			user['id'] = str(user['_id'])
			del user['_id']
			return user

	def update(self, data):
		user = self.user_collection.find_one({'_id': ObjectId(data['id'])})
		if user != None:
			for key in user: 
				if key != '_id': user[key] = data[key]
			user_collection.save(user)
			if not data.has_key('authority'):
				user['id'] = str(user['_id'])
				del user['_id']


if __name__ == '__main__':
	user = User()
	u = user.create({'username': 'xzz', 'password': '123'})
	print user.retrieve({'_id': u['_id']})