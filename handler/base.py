import tornado.web

class BaseHandler(tornado.web.RequestHandler):
	
    @porperty
    def db(self):
        return self.application.db
