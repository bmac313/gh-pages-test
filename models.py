from google.appengine.ext import db

class User(db.Model):
	username = db.StringProperty(required = True)
	pw_hash = db.StringProperty(required = True)
	email = db.StringProperty()
	
class Album(db.Model):
	title = db.StringProperty(required = True)
	artist = db.StringProperty(required = True)
	year = db.StringProperty(required = True)
	
class Review(db.Model):
	title = db.StringProperty(required = True)
	author = db.ReferenceProperty(required = True) # reference to a User
	body = db.TextProperty(required = True)
	rating = db.StringProperty(required = True) # recommended, not recommended, or maybe