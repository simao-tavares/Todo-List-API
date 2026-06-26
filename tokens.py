from flask_jwt_extended import create_access_token

def create_token(id: int):
    return create_access_token(identity = id)