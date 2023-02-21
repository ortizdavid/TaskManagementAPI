from config import *
from helpers.password_handler import *
from models.user import User
from helpers.http_code import *
from flask import jsonify, request, session

class AuthApi:

	@app.route(f'/{API_ROOT}/auth/login', methods=['POST'])
	def login():
		data = request.get_json()
		user_name = data['user_name']
		password = data['password']
		user = User.get_by_username(user_name)
		encrypted_password = user.password
		
		if PasswordHandler.check(encrypted_password, password):
			session['user_name'] = user_name
			session['password'] = encrypted_password
			logged_user = User.get_logged_user_basic()
			return jsonify({'data': logged_user.to_json(), 'message': 'Login Succeeded', 'success': True}), HTTP_CODE_OK
		else:
			return jsonify({'message': 'Invalid Username or Password', 'success': False}), HTTP_CODE_NOT_FOUND


	@app.route(f'/{API_ROOT}/auth/logout', methods=['GET'])
	def logout():
		if 'user_name' in session:
			session.pop('user_name')
			return jsonify({'message': 'Logout Succeeded', 'success': True}), HTTP_CODE_OK
		else:
			return jsonify({'message': 'Logout Failed', 'success': False}), HTTP_CODE_BAD_REQUEST


	@app.route(f'/{API_ROOT}/auth/user', methods=['GET'])
	def get_current_user():
		if 'user_name' in session:
			logged_user = User.get_logged_user_basic()
			return jsonify({'data': logged_user.to_json(), 'message': 'Logged User Found', 'success': True}), HTTP_CODE_OK
		else:
			return jsonify({'message': 'Logged User Not Found', 'success': False}), HTTP_CODE_NOT_FOUND