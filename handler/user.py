from base import BaseHandler
import json
import model.User as userModel

class RegisterHandler(BaseHandler):

	def post(self):
		#将body读取出来并转换为dict对象
		jparam = self.body
		usermodel = userModel(self.db)

		# 账号密码不能为空
		if not jparam['username'] or not jparam['password']:
			self.write({"status" : 0})
			return

		# 判断用户名是否已存在，已存在则注册失败
		if not usermodel.retrieve(jparam.items()[0]):
			usermodel.create(jparam)
			self.write({"status" : 1})
		else:
			self.write({"status" : 0})

class LoginHandler(BaseHandler):

	def post(self):
		#将body读取出来并转换为dict对象
		jparam = self.body
		usermodel = userModel(self.db)

		# 账号密码不能为空
		for key in jparam:
			if jparam[key] == '':
				self.write({"status" : 0})
				return

		#判断用户是否存在,若不存在则报错
		user = usermodel.retrieve(jparam)
		if not user:
			self.write({"status" : 0})
			return
		self.set_secure_cookie('id', user['id'])
		self.write({"status" : 1, "user" : user})

class RegisterinfoHandler(BaseHandler):

	def post(self):
		#将body读取出来并转换为dict对象
		jparam = self.body
		usermodel = userModel(self.db)

		#未登录不能进行操作
		if not self.current_user:
			self.set_status(401)
			return

		#性别不能为空
		if self.current_user == jparam['id'] and jparam['sex'] != '':
			user = usermodel.retrieve({'id': jparam['id']})
			#不能重复注册
			if user.has_key('sex'):
				self.write({"status" : 0})
			else:
				jparam.update({'authority': 0})
				usermodel.update(jparam)
				self.write({"status" : 1})
		else:
			self.write({"status" : 0})




class LogoutHandler(BaseHandler):

	def get(self):
		if self.current_user.has_key('id'):
			self.clear_cookie('id')
		self.write({"status": 1})


class ModifyinfoHandler(BaseHandler):

	def post(self):
		jparam = self.body
		usermodel = userModel(self.db)

		#未登录不能进行操作
		if not self.current_user:
			self.set_status(401)
			return

		#不能修改权限
		if jparam.has_key('authority'):
			self.write({"status" : 0})
			return

		#判断是否有修改权限
		if not self.current_user == jparam['id']:
			operate = usermodel.retrieve({'id': self.current_user})
			operated = usermodel.retrieve({'id': jparam['id']})
			if not self.authority(operate, operated):
				self.write({"status" : 0})
				return

		#需要修改的项不能为空
		for key in jparam:
			if jparam[key] == '':
				self.write({"status" : 0})

		usermodel.update(jparam)
		self.write({"status" : 1, "user": usermodel.retrieve({'id': jparam['id']})})

class ModifyauthorityHandler(BaseHandler):

	def post(self):
		jparam = self.body
		usermodel = userModel(self.db)

		#未登录不能进行操作
		if not self.current_user:
			self.set_status(401)
			return

		#判断是否有权限修改
		operate = usermodel.retrieve({'id': self.current_user})
		operated = usermodel.retrieve({'id': jparam['id']})
		if not self.authority(operate, operated):
			self.write({"status" : 0})
			return

		#只修改权限
		if not jparam.has_key('authority'):
			self.write({"status" : 0})
			return
		a = {'authority': jparam['authority']}
		usermodel.update(a)
		self.write({"status" : 1})


class GetusersHandler(BaseHandler):
	pass

class GetuserHandler(BaseHandler):
	pass
