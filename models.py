from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()



class Todo (db.Model):
    TodoID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TodoTitle = db.Column(db.String(50), nullable=True)
    TodoDescription = db.Column(db.String(150), nullable=True)
    TodoOwnerID = db.Column(db.Integer, db.ForeignKey('user.UserID'))
    TodoStatusID = db.Column(db.Integer, db.ForeignKey('todostatus.StatusID'), default = 1)
    TodoStartDate = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    TodoEndDate = db.Column(db.DateTime, nullable=True)


    def toJson(self):
        return {
            'ID': self.TodoID,
            'Title': self.TodoTitle,
            'Description': self.TodoDescription,
            'OwnerID': self.TodoOwnerID,
            'StatusID': self.TodoStatusID,
            'StartDate': self.TodoStartDate,
            'EndDate': self.TodoEndDate
        }


class User (db.Model):
    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserLogin = db.Column(db.String(50), nullable=True)
    UserPassword = db.Column(db.String(150), nullable=True)

    def toJson(self):
        return {
            'ID': self.UserID,
            'Login': self.UserLogin,
            'Password': self.UserPassword
        }

    def createPasswordHash (self, password):
        self.UserPassword = generate_password_hash(password)

    def decodePasswordHash (self, password):
        return check_password_hash(self.UserPassword, password)


class TokenBlocklistModel(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Jti = db.Column(db.String(36), nullable=False, index=True)
    CreatedAt = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())


    def toJson(self):
        return {
            'ID': self.ID,
            'JTI': self.Jti,
            'CreatedAt': self.CreatedAt
        }
    
    @classmethod
    def get_token(cls, jti):
        return db.session.query(TokenBlocklistModel.id).filter_by(jti=jti).scalar()
    

class TodoStatus (db.Model):
    __tablename__ = 'todostatus'
    StatusID = db.Column(db.Integer, primary_key=True)
    StatusDescription = db.Column(db.String(50), nullable=True)

    def toJson(self):
        return {
            'ID': self.StatusID,
            'Description': self.StatusDescription
        }
