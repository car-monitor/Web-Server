import tornado.web

class BaseHandler(tornado.web.RequestHandler):

    @porperty
    def db(self):
        return self.application.db

	def get_current_user(self):
		user_id = self.get_secure_cookie('id')
		if not user_id:
			return None
		return user_id
