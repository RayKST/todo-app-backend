from app import app
from datetime import datetime
from flask import request
from models import db, Todo
from redis_worker import jwt_required

@app.route('/api/task', methods=['GET', 'PUT', 'POST', 'DELETE'])
@jwt_required()
def task ():
    if request.method == 'GET':
        taskID = request.args.get('taskID')
        ownerID = request.args.get('ownerID')

        if (not (taskID)) and (not (ownerID)):
            tasks = Todo.query.all() 
            return {"tasks": [task.toJson() for task in tasks]}
        elif taskID:
            tasks = Todo.query.filter_by(TodoID = taskID)
            return {"tasks": [task.toJson() for task in tasks]}
        elif ownerID:
            tasks = Todo.query.filter_by(TodoOwnerID = ownerID)
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
        if 'Status' in data:
            task.TodoStatusID = data['Status']
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
                        TodoOwnerID = data['OwnerID'],
                        TodoStartDate = datetime.fromisoformat(data['StartDate']),
                        TodoEndDate = datetime.fromisoformat(data['EndDate'])
                        )
            
            db.session.add(task)
            db.session.commit()        
            return task.toJson(), 200
        
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500
        
    elif request.method == 'DELETE':
        taskID = request.args.get('taskID')
        task = Todo.query.filter_by(TodoID=taskID).first()

        if not task:
            return {"error": "Task not found"}, 404
        else:
            db.session.delete(task)
            db.session.commit()
            return {'message': 'Task deleted'}, 200
