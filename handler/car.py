from base import *
import json
import model.Car as Car


class RegisterHandler(BaseHandler):
	def post(self):
		if not self.current_user:
			self.set_status(401)
			return
		else:
			param = self.request.body.decode('utf-8')
			data = json.load(param)
			car = Car(self.db)
			if car.retrieve({'carPlate': data['carPlate']}) == None:
				carInfo = car.create(data)
				self.write({'status': 1, 'car': carInfo})
			else:
				self.write({'status': 0})


class RemoveHandler(BaseHandler):
	def post(self):
		if not self.current_user:
			self.set_status(401)
			return
		else:
			param = self.request.body.decode('utf-8')
			data = json.load(param)
			car = Car(self.db)
			car.delete(data)
			self.write({'status': 1})


class ModifyHandler(BaseHandler):
	def post(self):
		if not self.current_user:
			self.set_status(401)
			return
		else:
			param = self.request.body.decode('utf-8')
			data = json.load(param)
			car = Car(self.db)
			carInfo = car.update(data)
			if carInfo != None:
				self.write({'status': 1, 'car': carInfo})
			else:
				self.write({'status': 0})


class GetcarHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.set_status(401)
			return
		else:
			carid = self.get_argument('id', '')
			car = Car(self.db)
			carInfo = car.retrieve({'id': carid})
			if carInfo != None:
				order = Order(self.db)
				ordersInfo = order.retrieve({'carID': car['id']})
				self.write({'status': 1, 'car': carInfo, 'order': ordersInfo)
			else:
				self.write({'status': 0})


class GetcarsHandler(BaseHandler):
	def get(self):
		pass


class SendcarinfoHandler(BaseHandler):
	def post(self):
		pass