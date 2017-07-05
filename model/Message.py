from pymongo import MongoClient
from bson.objectid import ObjectId
import config


class Message:
	def __init__(self, client):
		#client = MongoClient(config.address, config.port)
		self.db = client[config.dbname]
		self.message_collection = self.db.message_collection

	def create(self, data):
		self.message_collection.insert(data)

	def retrieve(self, data):
		messages = self.message_collection.find({'senderid': ObjectId(data['id'])})
		messages.extend(self.message_collection.find({'receiverid': ObjectId(data['id'])}))
		