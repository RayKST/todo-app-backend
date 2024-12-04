from app import app
from flask import request
from flask_jwt_extended import (create_access_token)
from redis_worker import redis_instance, store_token_in_redis

from models import User

@app.route('/api/token', methods=['GET', 'PUT', 'POST', 'DELETE'])
def token ():
    if request.method == 'POST':
        data = request.get_json()
        username = data["Username"]
        password = data["Password"]
        
        user = User.query.filter_by(UserLogin=username).first()
        
        if not user or not user.decodePasswordHash(password):
            return {"Message": "Invalid username or password",
                    "Status": False}, 401

        access_token = create_access_token(identity=user.UserID)
        
        key = store_token_in_redis(access_token)
        return {
            "Access_Token": key,
            "Uid": user.UserID,
            "Status": True
        }, 201
    

@app.route('/api/redis')
def hello():
    redis_instance.incr('hits')
    counter = redis_instance.get('hits')
    return "Welcome to this webapage!, This webpage has been viewed "+counter+" time(s)"
