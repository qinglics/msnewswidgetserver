#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import webapp2
import cgi
import logging
import json

import newsdata

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class UpdateHandler(webapp2.RequestHandler):
    def get(self):
        data = newsdata.Data().getData()
        self.response.write(cgi.escape(json.dumps(data)))

    def post(self):
        self.response.write("Received data:\n")
        data = self.request.get('data')
        logging.error('data: ' + data)
        self.response.write(cgi.escape(data))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/update/', UpdateHandler)
], debug=True)
