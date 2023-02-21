from flask import Flask
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
	
RDMS = "postgresql"
DB_USER = "postgres"
DB_PASSWORD = "003334743LA032"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "db_task"
DB_URI = f"{RDMS}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

APP_PORT = "5000"
APP_ROOT = f"localhost:{APP_PORT}"
API_ROOT = "/api"

UPLOAD_DIR_IMGS = "uploads/imgs"
UPLOAD_DIR_DOCS = "uploads/docs"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'my-app'

db = SQLAlchemy()
db.init_app(app)

engine = create_engine(DB_URI)