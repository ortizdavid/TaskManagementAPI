from config import db, engine
from sqlalchemy import text

class Role(db.Model):

	__tablename__ = 'roles'

	role_id = db.Column(db.Integer, primary_key=True)
	role_name = db.Column(db.String(100))

	def __init__(self, role_name):
		self.role_name = role_name

	
	def save(self):
		db.session.add(self)
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()
	
	@classmethod
	def exists(cls, role_name):
		return bool(cls.query.filter_by(role_name=role_name).first())

	@classmethod
	def get_by_id(cls, id):
		return cls.query.filter_by(role_id=id).first()

	@classmethod
	def get_all(cls):
		return cls.query.all()

	def to_json(self):
		return {
			"role_id": self.role_id,
			"role_name": self.role_name
		}