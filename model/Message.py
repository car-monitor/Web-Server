from pymongo import MongoClient
from bson.objectid import ObjectId
import config


class Message:
	def __init__(self, db):
		self.message_collection = db.message_collection

	def create(self, data):
		self.message_collection.insert(data)

	def retrieve(self, data):
		messages1 = list(self.message_collection.find({'senderid': data['id']}))
		messages2 = list(self.message_collection.find({'receiverid': data['id']}))
		messages = messages1 + messages2
		for m in messages: del m['_id']
		return messages
