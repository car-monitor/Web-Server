from base import *
import json
from model.Department import Department
from model.Unit import Unit


class GetallunitsHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.set_status(401)
		else:
			unit = Unit(self.db)
			unitsInfo = unit.retrieve()
			self.write({'status': 1, 'units': unitsInfo})


class GetunitHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.set_status(401)
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
		else:
			data = json.loads(self.request.body.decode('utf-8'))
			unit = Unit(self.db)
			if unit.retrieve({'name': data['name']}) == None:
				unitInfo = unit.create(data)
				self.write({'status': 1, 'unit': unitInfo})
			else:
				self.write({'status': 0})

class GetalldepartmentsHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.set_status(401)
		else:
			department = Department(self.db)
			departmentsInfo = department.retrieve()
			self.write({'status': 1, 'departments': departmentsInfo})


class GetdepartmentHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.set_status(401)
		else:
			department = Department(self.db)
			departmentid = self.get_argument('id', '')
			departmentInfo = department.retrieve({'id': departmentid})
			if departmentInfo != None:
				self.write({'status': 1, 'department': departmentInfo})
			else:
				self.write({'status': 0})

class RegisterdepartmentHandler(BaseHandler):
	def post(self):
		if not self.current_user:
			self.set_status(401)
		else:
			data = json.loads(self.request.body.decode('utf-8'))
			department = Department(self.db)
			if department.retrieve({'name': data['name']}) == None:
				departmentInfo = department.create(data)
				self.write({'status': 1, 'department': departmentInfo})
			else:
				self.write({'status': 0})