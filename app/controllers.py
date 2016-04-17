# coding=utf-8

from flask import render_template, flash, redirect, g
from app import app
from .models import getData

@app.route('/')
@app.route('/index')
def index():
	data = getData()
	resData = '['
	for d in data:
		resData += '{id: ' + str(d.id) + ', data: \'' + d.data + '\'},'
	resData += ']'

	return render_template('index.html', data=resData)