from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Todo (db.Model):
    TodoID = db.Column(db.Integer, primary_key=True)
    TodoTitle = db.Column(db.String(50), nullable=False)
    TodoDescription = db.Column(db.String(150), nullable=True)
    TodoStartDate = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    TodoEndDate = db.Column(db.DateTime, nullable=True)


    def toJson(self):
        return {
            'ID': self.TodoID,
            'Title': self.TodoTitle,
            'Description': self.TodoDescription,
            'StartDate': self.TodoStartDate,
            'EndDate': self.TodoEndDate
        }