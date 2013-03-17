#coding=utf8

#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("jerry", "")
        comment = {
            "id": 1,
            "user": "qiu",
            "team": "jerry",
            "content": "only Test"
        }
        if not name :
            self.write("Welcome to Jerry!\n")
            self.write("欢迎来到Jerry!")
        else :
            self.write(tornado.escape.json_encode(comment))


class JerryHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("id", "")
        user = {}
        if not name :
            self.write("Hello jerry!\n")
            self.write("你好Jerry!")
        else :
            print "id : %s" % (name)
            user[name] = "Jerry路虎"
            self.write(tornado.escape.json_encode(user))


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/jerry", JerryHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
