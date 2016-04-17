# coding=utf-8

from app import db

class Data(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	data = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)

	def __repr__(self):
		return '<Data %r>' % (self.data)

def getData():
	return Data.query.all()