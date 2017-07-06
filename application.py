import os.path
import model.config as config
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymongo

import handler.user as user
import handler.car as car
import handler.company as company
import handler.info as info
import handler.order as order
import handler.render as render


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
            (r"/registerinfo", user.RegisterinfoHandler),
            (r"/logout", user.LogoutHandler),
            (r"/modifyinfo", user.ModifyinfoHandler),
            (r"/modifyauthority", user.ModifyauthorityHandler),
            (r"/getusers", user.GetusersHandler),
            (r"/getuser/(\w+)", user.GetuserHandler),
            (r"/registercar", car.RegisterHandler),
            (r"/removecar", car.RemoveHandler),
            (r"/modifycar", car.ModifyHandler),
            (r"/getcars", car.GetcarsHandler),
            (r"/getcar/(\w+)", car.GetcarHandler),
            (r"/sendcarinfo", car.SendcarinfoHandler),
            (r"/registerunit", company.RegisterunitHandler),
            (r"/getallunits", company.GetallunitsHandler),
            (r"/getunit/(\w+)", company.GetunitHandler),
            (r"/registerdepartment", company.RegisterdeparmentHandler),
            (r"/getalldepartment", company.GetalldepartmentHandler),
            (r"/getdepartment/(\w+)", company.GetdepartmentHandler),
            (r"/getallwarnings", info.GetallwarningsHandler),
            (r"/getwarning/(\w+)", info.GetwarningHandler),
            (r"/getmessage", info.GetmessageHandler),
            (r"/sendmessage", info.SendmessageHandler),
            (r"/registerorder", order.RegisterHandler),
            (r"/getorders", order.GetordersHandler),
            (r"/getorder/(\w+)", order.GetorderHandler),
            (r"/removeorder", order.RemoveHandler),
            (r"/modifyorder", order.ModifyHandler),
            (r"/(\w+)", render.RenderHandler),
            (r"/", tornado.web.RedirectHandler, {"url": "/newpath"})
        ]

        conn = MongoClient(config.address, config.port)
        self.db = conn[config.dbname]

        tornado.web.Application.__init__(self, handlers, **settings)



if (__name__=="__main__"):

    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
