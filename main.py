#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import webapp2
import cgi
import logging

class MainHandler(webapp2.RequestHandler):
    def get(self):
      self.response.write('Hello world!')

class UpdateHandler(webapp2.RequestHandler):
    def get(self):
      data = "this is a news item!";
      self.response.write(cgi.escape(data))

    def post(self):
      self.response.write("Received data:\n")
      data = self.request.get('data')
      logging.error('data: ' + data)
      self.response.write(cgi.escape(data))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/update/', UpdateHandler)
], debug=True)
