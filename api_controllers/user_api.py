from config import *
from helpers.file_uploader import *
from helpers.password_handler import *
from models.user import User
from models.role import Role
from helpers.http_code import *
from flask import jsonify, request, session

class UserApi:

	@app.route(f'/{API_ROOT}/users', methods=['GET'])
	def get_all_users():
		users = [user.to_json() for user in User.get_all()]
		num_rows = len(users)
		if num_rows == 0:
			return jsonify({'users': users, 'num_rows': num_rows, 'message': 'No Results Found', 'success': False}), HTTP_CODE_NOT_FOUND
		else:
			return jsonify({'users': users, 'num_rows': num_rows, 'message': 'Users Found', 'success': True}), HTTP_CODE_OK


	@app.route(f'/{API_ROOT}/users/<id>', methods=['GET'])
	def get_user(id):
		user = User.get_by_id(id)
		if user is None:
			return jsonify({'message': 'User Not found', 'success': False}), HTTP_CODE_NOT_FOUND
		else:
			return jsonify({'data': user.to_json(), 'success': True}), HTTP_CODE_OK


	@app.route(f'/{API_ROOT}/users', methods=['POST'])
	def add_user():
		data = request.get_json()
		role_id = data['role_id']
		user_name = data['user_name']
		password = data['password']
		image = ""

		if User.exists(user_name):
			return jsonify({'message': f"User '{user_name}' already exists", 'sucess': False}), HTTP_CODE_BAD_REQUEST
		try:
			user = User(role_id, user_name, password, image)
			user.save()
		except:
			return jsonify({'message': 'Error while adding user', 'success': False}) , HTTP_CODE_INTERNAL_ERROR
		return jsonify({'data': user.to_json(), 'message': 'User Added', 'success': True}), HTTP_CODE_CREATED


	@app.route(f'/{API_ROOT}/users/<id>', methods=['PUT'])
	def edit_user(id):
		user = User.get_by_id(id)
		data = request.get_json()
		data = request.get_json()
		role_id = data['role_id']
		user_name = data['user_name']
		password = data['password']
		image = ""
		try:
			if user is None:
				user = User(role_id, user_name, password, image)
			else:
				user.role_id = role_id
				user.user_name = user_name
				user.password = password
				user.image = image
			user.save()
		except:
			return jsonify({'message': 'Error while updating User', 'success': False}) , HTTP_CODE_INTERNAL_ERROR
		return jsonify({'data': user.to_json(), 'message': 'User Updated', 'success': True}), HTTP_CODE_CREATED


	@app.route(f'/{API_ROOT}/users/<id>', methods=['DELETE'])
	def delete_user(id):
		user = User.get_by_id(id)
		if user is None:
			return jsonify({'message': 'Error while deleting User', 'success': False}), HTTP_CODE_NOT_FOUND
		else:
			user.delete()
			return jsonify({'message': 'User Deleted!', 'success': True}), HTTP_CODE_OK


	@app.route(f'/{API_ROOT}/users/<id>/upload', methods=['POST'])
	def upload_image(id):
		user = User.get_by_id(id)
		if user is None:
			return jsonify({'message' : 'User not Found', 'success': False}), HTTP_CODE_NOT_FOUND
		else:
			uploader = FileUploader()
			image = uploader.upload_image('image', UPLOAD_DIR_IMGS)
			errors = uploader.errors
			if len(errors) > 0:
				return jsonify({'errors': errors, 'message' : 'Error while Uploading', 'success': False}), HTTP_CODE_BAD_REQUEST
			else:
				user.update_image(image, id)
				return jsonify({'file': image, 'message' : 'File successfully uploaded', 'success': True}), HTTP_CODE_CREATED