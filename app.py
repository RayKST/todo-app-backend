import config_app as ca

from flask import Flask
from flask_migrate import Migrate
from models import db
from security import config_app_cors, config_jwt_token

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ca.SQLITE_PATH

config_app_cors(app)
config_jwt_token(app)


db.init_app(app)

with app.app_context():
    db.create_all()

migrate = Migrate(app, db, render_as_batch=True)

from routes import task_routes, user_routes, token_routes, status_routes