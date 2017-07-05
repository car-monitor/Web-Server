import pymongo
import config

from pymongo import MongoClient
from bson.objectid import ObjectId

class Order:
	def __init__(self, client):
		#self.client = MongoClient(config.address, 27017)
		self.db = client[config.dbname]
		self.collection = self.db.order_collection

	def create(self, orderInformation):
		if self.collection != None:
			CarID = orderInformation['carID']
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
									'locationType': LocationType, 'startLongitude': StartLongitude,
									'startLatitude': StartLatitude, 'endLongitude': EndLongitude,
									'endLatitude': EndLatitude, 'isFinished': IsFinished,
									'startTime': StartTime, 'endTime': EndTime,
									'addressorName': AddressorName, 'addressorPhone': AddressorPhone,
									'addressorAddress': AddressorAddress, 'addresseeName': AddresseeName,
									'addresseePhone': AddresseePhone, 'addresseeAddress': AddresseeAddress,
									'sealExpect': SealExpect, 'sealCurrent': SealCurrent\
									})
			#rs = self.collection.find_one({'carID':CarID, 'driverId':DriverId})
			return {'status': 1}			# return {'status': 1, 'order':rs}  used to test
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
			rs_ = self.collection.find_one({'_id':ObjectId(string_id['id'])})
			if rs_ == None:
				return {'status': 1}
		else:
			return {'status': 0}

'''
test case:

if __name__ == '__main__':
	order_ = Order()
	dict_1 = {'carID': 56784, 'driverId': 89451,
			'startSite': 'GuangzhouRailwayStation', 'coordinateType': 'corrd',
			'locationType': 'y', 'startLongitude': 60.21,
			'startLatitude': 114.55, 'endLongitude': 65.45,
			'endLatitude': 88.54, 'isFinished': 0,
			'startTime': '2017/7/1 09:15:47', 'endTime': '2017/7/1 11:24:32',
			'addressorName': 'Young', 'addressorPhone': 13248781245,
			'addressorAddress': 'GuangzhoushiLibrary', 'addresseeName': 'Bob',
			'addresseePhone': 12487879852, 'addresseeAddress': 'GuangzhoushiScienceMuseum',
			'sealExpect': 'asd454w8few456fwe', 'sealCurrent': 'asdg4e86ge4re56'
			}
	result = order_.create(dict_1)
	if result['status'] == 1:
		print order_.retrieve({'id':result['order']['_id']})

	dict_2 = {'carID': 23484, 'driverId': 65548,
			'startSite': 'ShanghaiRailwayStation', 'coordinateType': 'corrd',
			'locationType': 'y', 'startLongitude': 75.65,
			'startLatitude': 131.48, 'endLongitude': 68.15,
			'endLatitude': 157.32, 'isFinished': 1,
			'startTime': '2017/6/27 21:34:05', 'endTime': '2017/6/28 00:02:10',
			'addressorName': 'Stephen', 'addressorPhone': 15687764541,
			'addressorAddress': 'ShanghaishiLibrary', 'addresseeName': 'Tomposon',
			'addresseePhone': 13548787450, 'addresseeAddress': 'ShanghaishiScienceMuseum',
			'sealExpect': 'fsd46wefr87et754', 'sealCurrent': 'hyer46w7ewe7rw4405w'
			}
	result_ = order_.create(dict_2)
	if result['status'] == 1:
		dict_3 = {'id':result_['order']['_id'], 'carID':25845,
					'isFinished':0, 'addresseePhone':15542792355,
					'sealExpect':'jyt468grew564aw'
					}
		rst = order_.update(dict_3)
		if rst['status'] == 1:
			order_.delete({'id':result['order']['_id']})	
'''

'''
	// The keyword function
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