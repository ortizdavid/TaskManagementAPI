from config import db, engine
from sqlalchemy import text

class Task(db.Model):

	__tablename__ = 'tasks'

	task_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer)
	task_name = db.Column(db.String(100))
	start_date = db.Column(db.Date)
	end_date = db.Column(db.Date)
	description = db.Column(db.String(300))

	def __init__(self, user_id, task_name, start_date, end_date, description):
		self.task_name = task_name
		self.description = description
		self.user_id = user_id
		self.start_date = start_date
		self.end_date = end_date
	
	def save(self):
		db.session.add(self)
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	@classmethod
	def exists(cls, user_id, task_name, start_date, end_date):
		return bool(cls.query.filter_by(user_id=user_id, task_name=task_name, start_date=start_date, end_date=end_date).first())
		
	@classmethod
	def get_by_id(cls, id):
		return cls.query.filter_by(task_id=id).first()
	
	@classmethod
	def get_by_user(cls, user_id):
		return cls.query.filter_by(user_id=user_id).all()

	@classmethod
	def get_by_date(cls, start_date, end_date):
		return cls.query.filter(cls.start_date.between(start_date, end_date)).all()
	
	@classmethod
	def get_all(cls):
		return cls.query.all()

	@classmethod
	def get_by_status(cls, status):
		with engine.connect() as conn:
			return conn.execute(text(f"SELECT * FROM view_user_tasks WHERE status = :status;"), {'status': status}).fetchall()

	@classmethod
	def search(cls, value):
		with engine.connect() as conn:
			return conn.execute(text(f"SELECT * FROM view_user_tasks WHERE user_id = :value"+	
								f" OR user_name = :value"+
								f" OR role_name = :value"), {'value': value}).fetchall()

	@classmethod
	def get_data_by_id(cls, id):
		with engine.connect() as conn:
			return conn.execute(text(f"SELECT * FROM view_user_tasks WHERE task_id = :id;"), {'id': id}).first()

	@classmethod
	def get_all_data(cls):
		with engine.connect() as conn:
			return conn.execute(text("SELECT * FROM view_user_tasks;")).fetchall()

	def to_json(self):
		task = Task.get_data_by_id(self.task_id)
		return {
			"task_id": task.task_id,
			"task_name": task.task_name,
			"description": task.description,
			"start_date": task.start_date,
			"end_date": task.end_date,
			"user_id": task.user_id,
			"status": task.status,
			"created_at": task.created_at,
			"created_at": task.created_at,
			"user_name": task.user_name,
			"role_name": task.role_name
		}