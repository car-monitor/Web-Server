from base import *
import json
import model.Order as order
import model.CarLocation as carLocation
import model.CarState as carState
import model.Warning as warning
import model.User as user

class GetordersHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.set_status(401)
			return
		else:
			orderDetail = []
			CarID = self.get_argument('carid', '')
			DriverID = self.get_argument('driverid', '')
			order_ = Order(self.db)
			carlocation = carLocation(self.db)
			orderlist = order_.retrieve({'carID': CarID, 'driverId':DriverID})
			for orderitem in orderlist:
				routelist = carlocation.retrieve({'id': orderitem['id'],
									'carID': CarID, 'driverId': DriverID})
				orderDetail.append({'order': orderitem, 'route': routelist})
			if orderDetail != None:
				self.write({'status': 1, 'orderdetails': orderDetail})
			else:
				self.write({'status': 0})


class GetorderHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.set_status(401)
			return
		else:
			userid = self.get_argument('id', '')
			order_ = order(self.db)
			carlocation = carLocation(self.db)
			carstate = carState(self.db)
			warn_ = warning(self.db)

			#search for the exact order
			
			orderInfo = order_.retrieve(userid)

			if orderInfo != None:    #Problem: how to decide whether orderInfo is None or not
				routelist = carlocation.retrieve({'id', orderInfo['id']})
				carstatelist = carstate.retrieve({'id': orderInfo['id']})
				warninglist = warn_.retrieve({'id': orderInfo['id']})
				self.write({'status':1, 'order':orderInfo, 'route':routelist,
								'carstatus':carstatelist, 'warning':warninglist})
			else:
				self.write({'status':0})

class RegisterHandler(BaseHandler):
	def post(self):
		if not self.current_user:
			self.set_status(401)
			return
		else:
			param = self.request.body.decode('utf-8')
			data = json.load(param)
			order_ = order(self.db)
			order_.create(data)

# Problem Removehandler and ModifyHandler authority
class RemoveHandler(BaseHandler):
	def post(self):
		if not self.current_user:
			self.set_status(401)
			return
		else:
			param = self.request.body.decode('utf-8')
			data = json.load(param)
			user_ = user(self.db)
			result = user_.retrieve(data)
			if result != None && result['authority'] >= 2:
				order_ = order(self.db)
				order_.delete(data)
				self.write({'status':1})
			else:
				self.write({'status':0})

class ModifyHandler(BaseHandler):
	def post(self):
		if not self.current_user:
			self.set_status(401)
			return
		else:
			userid = self.current_user
			param = self.request.body.decode('utf-8')
			data = json.load(param)
			user_ = user(self.db)
			currentuser = user_.retrieve(userid)
			order_ = order(self.db)
			if currentuser != None && currentuser['authority'] >= 2:
				result = order_update(data)
				self.write({'status': 1, 'order': result})
			else:
				result = order_.retrieve({'id':data['id']})
				self.write({'status': 0, 'order': result})