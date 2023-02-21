from config import *
from sqlalchemy import text
from flask import session
from config import db, engine

class User(db.Model):

	__tablename__ = 'users'

	user_id = db.Column(db.Integer, primary_key=True)
	role_id = db.Column(db.Integer)
	user_name = db.Column(db.String(100))
	password = db.Column(db.String(150))
	image = db.Column(db.String(150))

	def __init__(self, role_id, user_name, password, image):
		self.user_name = user_name
		self.password = password
		self.role_id = role_id
		self.image = image
	
	def save(self):
		db.session.add(self)
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	@classmethod
	def exists(cls, user_name):
		return bool(cls.query.filter_by(user_name=user_name).first())

	@classmethod
	def get_by_id(cls, id):
		return cls.query.filter_by(user_id=id).first()

	@classmethod
	def get_by_username(cls, user_name):
		return cls.query.filter_by(user_name=user_name).first()

	@classmethod
	def get_all(cls):
		return cls.query.all()

	@classmethod
	def get_logged_user(cls):
		user_name = session['user_name']
		password = session['password']
		return cls.get_user_data(user_name, password)

	@classmethod
	def get_logged_user_basic(cls):
		user_name = session['user_name']
		password = session['password']
		return cls.query.filter_by(user_name=user_name, password=password).first()

	@classmethod
	def get_user_data(cls, user_name, password):
		with engine.connect() as conn:
			return conn.execute(text(f"SELECT * FROM view_user_data WHERE user_name = :user_name AND password = :password;"), {'user_name': user_name, 'password': password}).first()

	@classmethod
	def search(cls, value):
		with engine.connect() as conn:
			return conn.execute(text(f"SELECT * FROM view_user_data WHERE user_id = :value"+	
								f" OR user_name = :value "+
								f" OR role_name = :value"), {'value': value}).fetchall()

	@classmethod
	def get_data_by_id(cls, id):
		with engine.connect() as conn:
			return conn.execute(text("SELECT * FROM view_user_data WHERE user_id = :id;"), {'id': id}).first()

	@classmethod
	def update_image(cls, image, id):
		with engine.begin() as conn:
			conn.execute(text(f"UPDATE users SET image = :image WHERE user_id = :id;"), {'image': image,  'id': id})

	@classmethod
	def get_all_data(cls):
		with engine.connect() as conn:
			return conn.execute(text("SELECT * FROM view_user_data;")).fetchall()

	def to_json(self):
		user = self.get_data_by_id(self.user_id)
		return {
			"user_id": user.user_id,
			"user_name": user.user_name,
			"password": user.password,
			"image": user.image,
			"created_at": user.created_at,
			"updated_at": user.updated_at,
			"role_id": user.role_id,
			"role_name": user.role_name
		}