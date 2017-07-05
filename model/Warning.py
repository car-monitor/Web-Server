import pymongo
import config 

from pymongo import MongoClient
from bson.objectid import ObjectId

class Warning:
	def __init__(self, client):
		#self.client = MongoClient(config.address, 27017)
		self.db = client[config.dbname]
		self.collection = self.db.warning_collection

	def create(self, warning_Information):
		if self.collection != None:
			StartID = warning_Information['startID']
			EndID = warning_Information['endID']
			Type = warning_Information['type']
			Status = warning_Information['status']
			WaybillID = warning_Information['waybillID']
			self.collection.insert({'startID': StartID, 'endID': EndID,
									'type':Type, 'status':Status,
									'waybillID':WaybillID
								})
			#rs = self.collection.find_one({'startID':StartID, 'endID':EndID})
			return {'status': 1}  # return {'status': 1, 'warning':rs}  used to test
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

'''
test case:

if __name__ == '__main__':
	warn = Warning()
	dict = {'startID':2312, 'endID':2345, 'type':'Overspeed',
			'status':0, 'waybillID':46878779
			}
	result = warn.create(dict)
	if result['status'] == 1:
		print warn.retrieve({'id':result['warning']['_id']})
'''