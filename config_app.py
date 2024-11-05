import os

SQLITE_PATH = os.environ.get('SQLITE_PATH', 'sqlite:///todo.db')

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', '6379'))
REDIS_PWD = os.environ.get('REDIS_PWD', 'redis')
REDIS_EXPIRATION_TIME = int(os.environ.get('REDIS_EXPIRATION_TIME', '3600'))