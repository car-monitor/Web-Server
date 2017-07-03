import pymongo
import config 

from pymongo import MongoClient
from bson.objectid import ObjectId

class CarState:
	def __init__(self, client):
		#client = MongoClient(config.address, config.port)
		self.db = client[config.dbname]
		self.collection = self.db.carState_collection

	def create(self, carState_information):
		if self.collection != None:
			CarID = carState_information['carID']
			DriverID = carState_information['driverID']
			Speed = carState_information['speed']
			Mileage = carState_information['mileage']
			Oil = carState_information['oil']
			LocationID = carState_information['locationID']
			Temperature = carState_information['temperature']
			Humidity = carState_information['humidity']
			Pressure = carState_information['pressure']
			Concentration = carState_information['concentration']
			AlertID = carState_information['alertID']
			PhotoURL = carState_information['photoURL']
			WaybillID = carState_information['waybillID']
			self.collection.insert({'carID':CarID, 'driverID':DriverID,
		    			   'speed':Speed, 'mileage':Mileage,
		    			   'oil':Oil, 'locationID':LocationID,
		    			   'temperature':Temperature, 'humidity':Humidity,
		    			   'pressure':Pressure, 'concentration':Concentration,
		    			   'alertID':AlertID, 'photoURL':PhotoURL,
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
			return {'status': 1, 'carstatus':rs}
		else:
			return {'status': 0}
