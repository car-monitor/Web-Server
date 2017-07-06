from base import *
import json
import model.User as userModel

class RegisterHandler(BaseHandler):

	def post(self):
		#将body读取出来并转换为dict对象
		param = self.request.body.decode('utf-8')
		jparam = json.load(param)
		usermodel = userModel(self.db)

		# 判断用户名是否已存在，已存在则注册失败
		if not usermodel.retrieve(jparam):
			usermodel.create(jparam)
			self.write({"status" : 1})
		else:
			self.write({"status" : 0})

class LoginHandler(BaseHandler):

	def post(self):
		#将body读取出来并转换为dict对象
		param = self.request.body.decode('utf-8')
		jparam = json.load(param)
		usermodel = userModel(self.db)

		#判断用户是否存在,若不存在则报错
		user = usermodel.retrieve(jparam)
		if not user:
			self.write({"status" : 0})
			return
		if user['password'] == jparam['password']:
			self.set_secure_cookie('id', user['id'])
			self.write({"status" : 1, "user" : user})




class LogoutHandler(BaseHandler):
	pass

class ModifyinfoHandler(BaseHandler):
	pass

class ModifyauthorityHandler(BaseHandler):
	pass

class GetusersHandler(BaseHandler):
	pass

class GetuserHandler(BaseHandler):
	pass
