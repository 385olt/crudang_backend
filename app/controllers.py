# coding=utf-8

from flask import jsonify, request
from app import app
from .models import getData, createData, saveData, deleteData, existsData

@app.route('/', methods=['GET'])
def index():
	return jsonify({'data': getData()})

@app.route('/', methods=['POST'])
def create():
	if not request.json or not 'data' in request.json:
		abort(400)
	newData = createData(request.json.get('data', ""))
	return jsonify({'data': newData}), 201

@app.route('/<int:id>', methods=['PUT'])
def save(id):
	if not request.json:
		abort(400)
	if 'data' in request.json and type(request.json['data']) != str:
		abort(400)
	if not existsData(id):
		abort(404)

	newData = saveData(id, request.json.get('data'))

	return jsonify({'data': newData})

@app.route('/<int:id>', methods=['DELETE'])
def delete(id):
	if not existsData(id):
		abort(404)
	deleteData(id)
	return jsonify({'result': True})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
