# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 01:11:43 2019

@author: MFarh
"""

import tornado.httpserver
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world this is Farhan")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8889)
    tornado.ioloop.IOLoop.instance().start() 