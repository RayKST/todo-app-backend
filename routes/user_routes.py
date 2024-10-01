from app import app
from flask import request
from models import User, db


@app.route('/api/user', methods=['GET', 'PUT', 'POST', 'DELETE'])
def user ():
    userID = request.args.get('userID')
    
    if request.method == 'GET':
        if not (userID):
            users = User.query.all() 
            return {"users": [user.toJson() for user in users]}
        else:
            users = User.query.filter_by(UserID = userID)
            return {"users": [task.toJson() for task in users]}
        
    elif request.method == 'PUT':

        data = request.get_json()
        user = User.query.filter_by(UserID=data['ID']).first()

        if not user:
            return {"error": "User not found"}, 404


        if 'Login' in data:
            user.UserLogin = data['Login']

        try:
            db.session.commit()        
            return user.toJson(), 200 
        except Exception as e:
            db.session.rollback() 
            return {"error": str(e)}, 500
        
    elif request.method == 'POST':
        data = request.get_json()
        userVerify = User.query.filter_by(UserLogin=data['Login']).first()

        if not userVerify:
            try:
                user = User(UserLogin = data['Login'])
                user.createPasswordHash(data['Password'])        
                
                db.session.add(user)
                db.session.commit()        
                return user.toJson(), 200
            
            except Exception as e:
                db.session.rollback()
                return {"error": str(e)}, 500
        else:
            return {"error": "Login already in the system"}, 400    
            
    elif request.method == 'DELETE':
        user = User.query.filter_by(UserID=userID).first()

        if not user:
            return {"error": "User not found"}, 404
        else:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted'}, 200




@app.route('/api/login', methods=['GET'])
def login ():
    if request.method == 'GET':
        data = request.get_json()
        user = User.query.filter_by(UserLogin=data['Login']).first()
        if (user.decodePasswordHash(data['Password'])):
            return {'Status': True}, 200
        else:
            return {'Status': False}, 400
