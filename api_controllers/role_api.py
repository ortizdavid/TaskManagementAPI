from config import *
from models.role import Role
from models.user import User
from helpers.http_code import *
from flask import jsonify, request, session

class RoleApi:
	
	@app.route(f'/{API_ROOT}/roles', methods=['GET'])
	def get_all_roles():
		roles = [role.to_json() for role in Role.get_all()]
		num_rows = len(roles)
		if num_rows == 0:
			return jsonify({'roles': roles, 'num_rows': num_rows, 'message': 'No Results Found', 'success': False}), HTTP_CODE_NOT_FOUND
		else:
			return jsonify({'roles': roles, 'num_rows': num_rows, 'message': 'Roles Found', 'success': True}), HTTP_CODE_OK


	@app.route(f'/{API_ROOT}/roles/<id>', methods=['GET'])
	def get_role(id):
		role = Role.get_by_id(id)
		if role is None:
			return jsonify({'message': 'Role Not found', 'success': False}), HTTP_CODE_NOT_FOUND
		else:
			return jsonify({'data': role.to_json(), 'message': 'Role Found', 'success': True}), HTTP_CODE_OK


	@app.route(f'/{API_ROOT}/roles', methods=['POST'])
	def add_role():
		data = request.get_json()
		role_name = data['role_name']
		if Role.exists(role_name):
			return jsonify({'message': 'Role already exists', 'sucess': False}), HTTP_CODE_BAD_REQUEST
		try:
			role = Role(role_name)
			role.save()
		except:
			return jsonify({'message': 'Erro while adding Role', 'success': False}), HTTP_CODE_INTERNAL_ERROR
		return jsonify({'data': role.to_json(), 'message': 'Role Added', 'success': True}), HTTP_CODE_CREATED


	@app.route(f'/{API_ROOT}/roles/<id>', methods=['PUT'])
	def edit_role(id):
		role = Role.get_by_id(id)
		data = request.get_json()
		role_name = data['role_name']
		try:
			if role is None:
				role = Role(role_name)
			else:
				role.role_name = role_name
			role.save()
		except:
			return jsonify({'message': 'Erro while updating Role', 'success': False}) , HTTP_CODE_INTERNAL_ERROR
		return jsonify({'data': role.to_json(), 'message': 'Role Updated', 'success': True}), HTTP_CODE_CREATED


	@app.route(f'/{API_ROOT}/roles/<id>', methods=['DELETE'])
	def delete_role(id):
		role = Role.get_by_id(id)
		if role is None:
			return jsonify({'message': 'role Not Found', 'success': False}), HTTP_CODE_NOT_FOUND
		else:
			role.delete()
			return jsonify({'message': 'role Deleted!', 'success': True}), HTTP_CODE_OK