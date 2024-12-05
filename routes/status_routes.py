from app import app
from flask import request
from models import TodoStatus


@app.route('/api/todo_status', methods=['GET', 'PUT', 'POST', 'DELETE'])
def status ():
    todoStatusID = request.args.get('todoStatusID')
    
    if request.method == 'GET':
        if not (todoStatusID):
            todoStatus = TodoStatus.query.all() 
            return {"todo_status": [status.toJson() for status in todoStatus]}
        else:
            todoStatus = TodoStatus.query.filter_by(StatusID = todoStatusID)
            return {"todo_status": [status.toJson() for status in todoStatus]}