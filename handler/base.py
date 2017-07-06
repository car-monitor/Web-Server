import tornado.web

class BaseHandler(tornado.web.RequestHandler):

    @porperty
    def db(self):
		# 获取数据库连接
        return self.application.db

    @property
    def body(self):
        param = self.request.body.decode('utf-8')
		jparam = json.load(param)
        return jparam

    # 判断是否有权限
    def authority(self, operate, operated):

        jparam = self.body()

        if not operate or not operated:
            return False

        if operate['authority'] == 2 or operate['authority'] == 3 and operated['authority'] < operate['authority']:
            return True
        return False

	def get_current_user(self):
		# 通过cookie获取当前用户
		user_id = self.get_secure_cookie('id')
		if not user_id:
			return None
		return user_id
