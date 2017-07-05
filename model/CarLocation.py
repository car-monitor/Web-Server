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
		if self.collection != None:
			CarID = carLocation_information['carID']
			WaybillID = carLocation_information['waybillID']
			Time = carLocation_information['time']
			CoordinateType = carLocation_information['coordinateType']
			LocationType = carLocation_information['locationType']
			Longitude = carLocation_information['longitude']
			Latitude = carLocation_information['latitude']
			DriverId = carLocation_information['driverId']
			PhotoURL = carLocation_information['photoURL']
			self.collection.insert({'carID':CarID, 'waybillID':WaybillID,
									'time':Time, 'coordinateType':CoordinateType,
									'locationType':LocationType, 'longitude':Longitude,
									'latitude':Latitude, 'driverId':DriverId,
									'photoURL':PhotoURL
									})
			#rs = self.collection.find_one({'carID':CarID, 'driverId':DriverId})
			return {'status': 1}    # return {'status': 1, 'carLocation':rs} used to test
		else:
			return {'status': 0}

	def retrieve(self, string_id):
		rs = self.collection.find_one({'_id':ObjectId(string_id['id'])})

		if rs != None:
			rs['id'] = str(rs['_id'])
			del rs['_id']
			return {'status': 1, 'route':rs}
		else:
			return {'status': 0}

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