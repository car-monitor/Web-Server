from base import *
import json
import model.Department as Department
import model.Unit as Unit


class GetallunitsHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.set_status(401)
			return
		else:
			unit = Unit(self.db)
			unitsInfo = unit.retrieve()
			self.write({'status': 1, 'units': unitsInfo})


class GetunitHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.set_status(401)
			return
		else:
			unit = Unit(self.db)
			unitid = self.get_argument('id', '')
			unitInfo = unit.retrieve({'id': unitid})
			if unitInfo != None:
				self.write({'status': 1, 'unit': unitInfo})
			else:
				self.write({'status': 0})


class RegisterunitHandler(BaseHandler):
	def post(self):
		if not self.current_user:
			self.set_status(401)
			return
		else:
			param = self.request.body.decode('utf-8')
			data = json.load(param)
			unit = Unit(self.db)
			if unit.retrieve({'name': data['name']}) == None:
				unitInfo = unit.create(data)
				self.write({'status': 1, 'unit': unitInfo})
			else:
				self.write({'status': 0})

class GetalldepartmentHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.set_status(401)
			return
		else:
			department = Department(self.db)
			departmentsInfo = department.retrieve()
			self.write({'status': 1, 'departments': departmentsInfo})


class GetdepartmentHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.set_status(401)
			return
		else:
			department = Department(self.db)
			departmentid = self.get_argument('id', '')
			departmentInfo = department.retrieve({'id': departmentid})
			if departmentInfo != None:
				self.write({'status': 1, 'department': departmentInfo})
			else:
				self.write({'status': 0})

class RegisterdeparmentHandler(BaseHandler):
	def post(self):
		if not self.current_user:
			self.set_status(401)
			return
		else:
			param = self.request.body.decode('utf-8')
			data = json.load(param)
			department = Department(self.db)
			if department.retrieve({'name': data['name']}) == None:
				departmentInfo = department.create(data)
				self.write({'status': 1, 'department': departmentInfo})
			else:
				self.write({'status': 0})