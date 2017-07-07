import pymongo
import config 

from pymongo import MongoClient
from bson.objectid import ObjectId

class CarState:
	def __init__(self, client):
		#self.client = MongoClient(config.address, 27017)
		self.db = client[config.dbname]
		self.collection = self.db.carState_collection

	def create(self, carState_information):
		carstateid = self.collection.insert(carState_information)
		carState_information['id'] = str(carstateid)
		del carState_information['_id']
		return carState_information


	def retrieve(self, data):
		flag_carid = False
		flag_driverid = False
		if data.has_key('id'):    # Or if data.has_key('waybillId')
			data['waybillID'] = ObjectId(data['id'])
			del data['id']

		result = self.collection.find({'waybillID': data['waybillID']})
		Dict = []
		if result != None:
			for item in result:
				item['id'] = str(item['_id'])
				del item['_id']
				Dict.append(item)
			return Dict

'''
test case:

if __name__ == '__main__':
	carstate = CarState()
	dict = {'carID':'26546', 'driverID':'448714',
			'speed':50, 'mileage':954,
			'oil':14, 'locationID':2654,
			'temperature':40, 'humidity':68,
			'pressure':210, 'concentration':2.3,
			'alertID':12475, 'photoURL':'~/Desktop/Photos/photo_7.png',
			'waybillID':56787
			}
	result = carstate.create(dict)
	if result['status'] == 1:
		print carstate.retrieve({'id':result['carState']['_id']})
'''