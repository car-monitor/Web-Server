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
		messages1 = list(self.message_collection.find({'senderid': data['id']}))
		messages2 = list(self.message_collection.find({'receiverid': data['id']}))
		messages = messages1 + messages2
		for m in messages: del m['_id']
		return messages


if __name__ == '__main__':
	client = MongoClient(config.address, config.port)
	collection = Message(client)
	collection.create({'senderid': '595cf2ff99616e517ca52142'})
	print collection.retrieve({'id': '595cf2ff99616e517ca52142'})

		