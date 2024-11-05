from flask import request, make_response
import config_app as ca
from functools import wraps
from redis import Redis
import hashlib

redis_instance = Redis(host=ca.REDIS_HOST, port=ca.REDIS_PORT, password=ca.REDIS_PWD, decode_responses=True)

def store_token_in_redis(token):
    key = hashlib.md5(token.encode()).hexdigest()
    redis_instance.set(key , token, ex=ca.REDIS_EXPIRATION_TIME)
    return key

def get_token_from_redis(access_key):
    return redis_instance.get(access_key)

def jwt_required():
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header or not auth_header.startswith('Bearer '):
                return make_response({"msg": "Missing or invalid Authorization header"}, 400)

            access_key = auth_header.split(" ")[1]
            if not access_key:
                return make_response({"message": "Missing access key"}, 400)

            token = get_token_from_redis(access_key)
            if not token:
                return make_response({"message": "Invalid access key"}, 401)

            return fn(*args, **kwargs)
        return wrapper
    return decorator