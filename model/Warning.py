import pymongo
import config 

from pymongo import MongoClient
from bson.objectid import ObjectId

class Warning:
	def __init__(self, client):
		#client = MongoClient(config.address, config.port)
		self.db = client[config.dbname]
		self.collection = self.db.warning_collection

	def create(self, warning_Information):
		if self.collection != None:
			StartID = warning_Information['startID']
			EndID = warning_Informaion['endID']
		  	Type = warning_Information['type']
		  	Status = warning_Information['status']
		  	WaybillID = warning_Information['waybillID']
		  	self.collection.insert({'startID': StartID, 'endID': EndID,
		  							'type':Type, 'status':Status,
		  							'waybillID':WaybillID
		  						  })
			return {'status': 1}
		else:
			return {'status': 0}

	def retrieve(self, string_id):
		rs = self.collection.find_one({'_id':ObjectId(string_id['id'])})

		if rs != None:
			rs['id'] = str(rs['_id'])
			del rs['_id']
			return {'status': 1, 'warning':rs}
		else:
			return {'status': 0}
