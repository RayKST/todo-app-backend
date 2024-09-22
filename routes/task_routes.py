from app import app
from models import Todo


@app.route('/api/task', methods=['GET'])
def index ():
    tasks = Todo.query.all() 
    #print(request.args.get('id', default = 1, type = int))
    return {"tasks": [task.toJson() for task in tasks]}