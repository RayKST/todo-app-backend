import config_app as ca

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ca.SQLITE_PATH
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


db.init_app(app)

with app.app_context():
    db.create_all()

migrate = Migrate(app, db)

from routes import task_routes, user_routes, token_routes