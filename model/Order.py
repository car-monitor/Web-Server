import pymongo
import config

from pymongo import MongoClient
from bson.objectid import ObjectId

class Order:
	def __init__(self, client):
		#client = MongoClient(config.address, config.port)
		self.db = client[config.dbname]
		self.collection = self.db.order_collection

	def create(self, orderInformation):
	   	if self.collection != None:
	   		CarID = orderInformation['carId']
			DriverId = orderInformation['driverId']
			StartSite = orderInformation['startSite']
			CoordinateType = orderInformation['coordinateType']
			LocationType = orderInformation['locationType']
			StartLongitude = orderInformation['startLongitude']
			StartLatitude = orderInformation['startLatitude']
			EndLongitude = orderInformation['endLongitude']
			EndLatitude = orderInformation['endLatitude']
			IsFinished = orderInformation['isFinished']
	    	StartTime = orderInformation['startTime']
	    	EndTime = orderInformation['endTime']
	    	AddressorName = orderInformation['addressorName']
	    	AddressorPhone = orderInformation['addressorPhone']
	    	AddressorAddress = orderInformation['addressorAddress']
	    	AddresseeName = orderInformation['addresseeName']
	    	AddresseePhone = orderInformation['addresseePhone']
	    	AddresseeAddress = orderInformation['addresseeAddress']
	    	SealExpect = orderInformation['sealExpect']
	    	SealCurrent = orderInformation['sealCurrent']
	    	self.collection.insert({'carID': CarID, 'driverId': DriverId,
						   'startSite': StartSite, 'coordinateType': CoordinateType,
						   'locationType': LocationType, 'startLongitude': startLongitude,
						   'startLatitude': startLatitude, 'endLongitude': EndLongitude,
						   'endLatitude': EndLatitude, 'isFinished': isFinished,
	    				   'startTime': StartTime, 'endTime': EndTime,
	    				   'addressorName': AddressorName, 'addressorPhone': AddressorPhone,
	    				   'addressorAddress': AddressorAddress, 'addresseeName': AddresseeName,
	   					   'addresseePhone': AddresseePhone, 'addresseeAddress': AddresseeAddress,
	   					   'sealExpect': SealExpect, 'sealCurrent': SealCurrent})
			return {'status': 1}
		else:
			return {'status': 0}

	def retrieve(self, string_id):
		rs = self.collection.find_one({'_id':ObjectId(string_id['id'])})

		if rs != None:
			rs['id'] = str(rs['_id'])
			del rs['_id']
			return {'status': 1, 'order': rs}
		else:
			return {'status': 0}

'''
	'// The keyword function'
	def retrieve_all(self, reterieve_information):
		collection = self.db.order_collection

		CarID = reterieve_information['carid']
		DriverId = reterieve_information['driverid']

		rs = collection.find({'carID':CarID, 'driverID':DriverId})

		if rs:
			return {'status': 1, 'orderdetails':rs}
		else:
			return {'status': 0}
'''

	def update(self, update_information):
		passid = update_information['id']
		rs = self.collection.find_one({'_id':ObjectId(passid)})

		if rs != None:
			for key in update_information:
				if key != 'id':
					rs[key] = update_information[key]
					self.db.order_collection.save(rs)
			rs_1 = self.collection.find_one({'_id':ObjectId(passid)})
			return {'status': 1, 'order':rs_1}
		else:
			return {'status': 0, 'order': rs}

	def delete(self, string_id):
		rs = self.collection.find_one({'_id':ObjectId(string_id['id'])})

		if rs:
			self.collection.remove({'_id':ObjectId(string_id['id'])})
			return {'status': 1}
		else:
			return {'status': 0}
