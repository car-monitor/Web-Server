import tornado.web

class BaseHandler(tornado.web.RequestHandler):

    @porperty
    def db(self):
		# 获取数据库连接
        return self.application.db

	def get_current_user(self):
		# 通过cookie获取当前用户
		user_id = self.get_secure_cookie('id')
		if not user_id:
			return None
		return user_id
