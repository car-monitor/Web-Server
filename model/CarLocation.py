import pymongo
import config 

from pymongo import MongoClient
from bson.objectid import ObjectId

class CarLocation:
	def __init__(self, client):
		#self.client = MongoClient(config.address, 27017)
		self.db = client[config.dbname]
		self.collection = self.db.carLocation_collection

	def create(self, carLocation_information):
		carloactionId = self.collection.insert(carLocation_information)
		carLocation_information['id'] = str(carloactionId)
		del carLocation_information['_id']
		return carLocation_information

# Problem
	def retrieve(self, data):
		flag_waybillid = False
		flag_carid = False
		flag_driverid = False
		if data.has_key('id'):    # Or if data.has_key('waybillId')
			data['waybillID'] = ObjectId(data['id'])
			del data['id']

		if data.has_key('carid'):
			flag_carid = True
			data['carID'] = ObjectId(data['carid'])
			del data['carid']

		if data.has_key('driverid'):
			flag_driverid = True
			data['driverId'] = ObjectId(data['driverid'])
			del data['driverid']

		result = {}
		if flag_carid == True && flag_driverid == False:
			result = self.collection.find({'waybillID': data['waybillID'],
								'carID': data['carID']})
		else if flag_carid == False && flag_driverid == True:
			result = self.collection.find({'waybillID': data['waybillID'],
								'driverid': data['driverid']})
		else if flag_carid == True && flag_driverid == True:
			result = self.collection.find({'waybillID': data['waybillID'],
								'carID': data['carID'], 'driverid': data['driverid']})
		else if flag_carid == False && flag_driverid == False:
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
	car_location = CarLocation()
	dict = {'carID':16498, 'waybillID':23848,
			'time':'2017/7/7 15:42:23', 'coordinateType':'coord',
			'locationType':'y', 'longitude':40.67,
			'latitude':124.26, 'driverId':35448,
			'photoURL':'~/Desktop/Photos/photo_12.png'
			}
	result = car_location.create(dict)
	if result['status'] == 1:
		print car_location.retrieve({'id':result['carLocation']['_id']})
'''