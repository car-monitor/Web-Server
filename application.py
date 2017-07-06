import os.path
import model.config as config
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymongo

import handler.user as user


from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):

    def __init__(self):

        settings = dict(
            cookie_secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E="
            # xsrf_cookies=True
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static")
        )

        handlers = [
            (r"/regsiter", user.RegisterHandler),
            (r"/login", user.LoginHandler),
            (r"/logout", ),
            (r"/modifyinfo", ),
            (r"/modifyauthority", ),
            (r"/getusers", ),
            (r"/getuser/(\w+)", ),
        ]

        conn = MongoClient(config.address, config.port)
        self.db = conn[config.dbname]

        tornado.web.Application.__init__(self, handlers, **settings)



if (__name__=="__main__"):

    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
