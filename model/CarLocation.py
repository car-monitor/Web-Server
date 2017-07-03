import pymongo
import config 

from pymongo import MongoClient
from bson.objectid import ObjectId

class CarLocation:
	def __init__(self, client):
		#client = MongoClient(config.address, config.port)
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
			return {'status': 1}
		else:
			return {'status': 0}

	def retrieve(self, string_id):
		rs = self.connection.find_one({'_id':ObjectId(string_id['id'])})

		if rs != None:
			rs['id'] = str(rs['_id'])
			del rs['_id']
			return {'status': 1, 'route':rs}
		else:
			return {'status': 0}
'''
	// the keyword function
	def retrieve(self, retrieve_information):
		connection = self.db.carLocation_collection
		CarID = retrieve_information['carid']
		DriverId = retrieve_information['driverid']

		rs = connection.find({'cardID':CarID, 'driverId':DriverId})

		if rs:
			return {'status': 1, 'route':rs}
		else:
			return {'status': 0}
'''
