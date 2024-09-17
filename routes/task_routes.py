from app import app
from models import Todo
import json


@app.route('/', methods=['GET'])
def index ():
    print(Todo.query.all()[0].returnJson())
    return {
        'statusCode': 200
    }