from app import app
from datetime import datetime
from flask import request
from models import db, Todo


@app.route('/api/task', methods=['GET', 'PUT', 'POST'])
def index ():
    taskID = request.args.get('taskID')
    if request.method == 'GET':
        if not (taskID):
            tasks = Todo.query.all() 
            return {"tasks": [task.toJson() for task in tasks]}
        else:
            tasks = Todo.query.filter_by(TodoID = taskID)
            return {"tasks": [task.toJson() for task in tasks]}
    
    elif request.method == 'PUT':

        data = request.get_json()
        task = Todo.query.filter_by(TodoID=data['ID']).first()

        if not task:
            return {"error": "Task not found"}, 404
        
        # Update the task attributes with new data
        if 'Title' in data:
            task.TodoTitle = data['Title']
        if 'Description' in data:
            task.TodoDescription = data['Description']
        if 'StartDate' in data:
            task.TodoStartDate = datetime.fromisoformat(data['StartDate'])
        if 'EndDate' in data:
            task.TodoEndDate = datetime.fromisoformat(data['EndDate'])   
        
        try:
            db.session.commit()        
            return task.toJson(), 200  # Return updated task
        except Exception as e:
            db.session.rollback()  # Rollback the session on error
            return {"error": str(e)}, 500  # Return the error message


    elif request.method == 'POST':
        data = request.get_json()
        try:
            task = Todo(TodoTitle = data['Title'], 
                        TodoDescription = data['Description'],
                        TodoStartDate = data['StartDate'],
                        TodoEndDate = data['EndDate']
                        )
            
            db.session.add()
            db.session.commit()        
            return task.toJson(), 200
        
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500