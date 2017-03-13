#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2, jinja2, os, re
from google.appengine.ext import db
from models import User
import hashutils

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class SiteHandler(webapp2.RequestHandler):
	def get_user_by_name(self, username):
		user = db.GqlQuery("SELECT * FROM User WHERE username=%s" % username)
		if user:
			return user.get()
	
	def login_user(self, user):
		pass
		
	def logout_user(self, user):
		pass
	

class IndexHandler(SiteHandler):
    def get(self):
        self.response.write('Hello world!')
		
class ViewUserHandler(SiteHandler):
	""" 
	Handles all requests to view a user's profile.
	Shows a public profile if not logged in. If logged in, give the user options to
	edit their profile.
	"""
	def get(self, username=""):
		self.response.write("Custom route is working! User profile to be displayed: %s" % username)

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
	webapp2.Route('/u/<username:[a-zA-Z0-9_-]{3,20}>', ViewUserHandler)
], debug=True)
