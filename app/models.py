# coding=utf-8

from app import db

class Data(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	data = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)

	def __repr__(self):
		return '<Data ' + str(self.id) + ' ' + self.data + '>'

def data2dict(data):
	if isinstance(data, list):
		return [data2dict(x) for x in data]

	d = dict()
	d['id'] = data.id
	d['data'] = data.data
	return d

def existsData(id):
	return db.session.query(db.exists().where(Data.id == id)).scalar()

def getData():
	return data2dict(Data.query.all())

def createData(data):
	data = Data(data=data)
	db.session.add(data)
	db.session.commit()
	return data2dict(Data.query.filter_by(data=data.data).order_by(Data.id.desc()).first())

def saveData(id, data):
	mydata = Data.query.get(id)
	mydata.data = data
	db.session.commit()
	return data2dict(mydata)

def deleteData(id):
	mydata = Data.query.get(id)
	db.session.delete(mydata)
	db.session.commit()
