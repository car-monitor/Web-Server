from base import *
import json
import model.WarningDict as warningDict
import model.Message as message
import model.User as user

class GetallwarningsHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.set_status(401)
			return
		else:
			warningdict = warningDict(self.db)
			result = warningdict.retrieve()
			self.write({'status': 1, 'warnings': result})

class GetwarningHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.set_status(401)
			return 
		else:
			warningid = self.get_argument('id', '')
			warningdict = warningDict(self.db)
			result = warningdict.retrieve({'id': warningid})
			if result != None:
				self.write({'status': 1, 'warning': result})
			else:
				self.write({'status': 0})

class GetmessageHandler(BaseHandler):
	def get(self):
		userid = self.current_user
		if userid == None:
			self.set_status(401)
		else:
			Infos = []
			senderInfos = []
			receiverInfos = []
			message_ = message(db.self)
			user_ = user(db.self)
			messagelist = message_.retrieve(userid)
			userInfo = user_.retrieve(userid)

			for message_item in messagelist:
				if str(message_item['senderid']) == userid['id']:
					info_item = {'type': message_item['type'], 'sender': userInfo,
						'title': message_item['title'], 'content': message_item['content']}
					senderInfos.append(info_item)
				else if str(message_item['receiverid']) == userid['id']:
					info_item = {'type': message_item['type'], 'receiver': userInfo,
						'title': message_item['title'], 'content': message_item['content']}
					receiverInfos.append(info_item)
			Infos = senderInfos + receiverInfos
			if Infos != None:
				self.write({'status': 1, 'infos': Infos})
			else:
				self.write({'status': 0})

class SendmessageHandler(BaseHandler):
	def post(self):
		if self.current_user:
			self.set_status(401)
			return
		else:
			userid = self.current_user
			flag = True
			param = self.request.body.decode('utf-8')
			data = json.load(param)
			message_ = message(self.db)
			data['id'] = userid['id']
			for key in data:
				if data.get(key, 0) == 0:    #decide whether the value is None
					flag = False
					break
			if flag == True:
				message_.create(data)
				self.write({'status':1})
			else:
				self.write({'status':0})
