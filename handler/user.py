from base import *
import json
import model.User as userModel

class RegisterHandler(BaseHadnler):

	def post(self):
		#将body读取出来并转换为dict对象
		param = self.request.body.decode('utf-8')
		jparam = json.load(param)
		usermodel = userModel(self.db)
		jparam['username']
