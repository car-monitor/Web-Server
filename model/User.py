from pymongo import MongoClient
from bson.objectid import ObjectId
import config


class User:
	def __init__(self, client):
		#client = MongoClient(config.address, config.port)
		self.db = client[config.dbname]
		self.user_collection = self.db.user_collection

	def create(self, data):
		return self.user_collection.insert({'username': data['username'], 'password': data['password']})

	def retrieve(self, data):
		#ignore the function of keyword
		if data.has_key('authority'):
			users = self.user_collection.find({'authority': data['authority']})
			for user in users:
				user['id'] = str(user['_id'])
				del user['_id']
			return users
		else:
			user = self.user_collection.find_one({'_id': ObjectId(data['id'])})
			if user != None:
				user['id'] = str(user['_id'])
				del user['_id']
			return user

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


if __name__ == '__main__':
	client = MongoClient(config.address, config.port)
	collection = User(client)
	uid = collection.create({'username': 'xzz', 'password': '123'})
	print collection.retrieve({'id': uid})
	print collection.update({'id': uid, 'username': 'zzx'})
