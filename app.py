import os.path
import model.config as config
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from pymongo import MongoClient
import handler.car as CarHandler
import handler.company as CompanyHandler


define("port", default=8000, help="run on the given port", type=int)


class Application(tornado.web.Application):

    def __init__(self):

        settings = dict(
            cookie_secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
            # xsrf_cookies=True
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static")
        )

        handlers = [
            (r'/register', CarHandler.RegisterHandler),
			(r'/remove', CarHandler.RemoveHandler),
			(r'/modify', CarHandler.ModifyHandler),
			(r'/getcar', CarHandler.GetcarHandler),
			#(r'/getcars', CarHandler.GetcarsHandler)
			(r'/getallunits', CompanyHandler.GetallunitsHandler),
			(r'/getunit', CompanyHandler.GetunitHandler),
			(r'/registerunit', CompanyHandler.RegisterunitHandler),
			(r'/getalldepartments', CompanyHandler.GetalldepartmentsHandler),
			(r'/getdepartment', CompanyHandler.GetdepartmentHandler),
			(r'/registerdepartment', CompanyHandler.RegisterdepartmentHandler)
        ]

        conn = MongoClient(config.address, config.port)
        self.db = conn[config.dbname]

        tornado.web.Application.__init__(self, handlers, **settings)


if (__name__=="__main__"):

    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    print 'listen at 8000'
    tornado.ioloop.IOLoop.instance().start()