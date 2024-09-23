from app import app
from datetime import datetime
from flask import request
from models import db, Todo


@app.route('/api/task', methods=['GET', 'PUT'])
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
            task.Title = data['Title']
        if 'Description' in data:
            task.Description = data['Description']
        
        #task.StartDate = datetime.now()
        
        #task.EndDate = datetime.now()
        
        
        try:
            db.session.commit()        
            return task.toJson(), 200  # Return updated task
        except Exception as e:
            db.session.rollback()  # Rollback the session on error
            return {"error": str(e)}, 500  # Return the error message