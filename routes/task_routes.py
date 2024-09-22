from app import app
from flask import request
from models import Todo


@app.route('/api/task', methods=['GET'])
def index ():
    taskID = request.args.get('taskID')
    if not (taskID):
        tasks = Todo.query.all() 
        return {"tasks": [task.toJson() for task in tasks]}
    else:
        tasks = Todo.query.filter_by(TodoID = taskID)
        return {"tasks": [task.toJson() for task in tasks]}