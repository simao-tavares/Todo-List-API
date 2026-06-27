from flask_jwt_extended import create_access_token, decode_token
from jwt import ExpiredSignatureError, DecodeError, InvalidTokenError

def create_token(id: int):
    return create_access_token(identity = str(id))

def validate_token(token: str):
    try:
        token_decoded = decode_token(token)
        return token_decoded['sub']
    except (ExpiredSignatureError, DecodeError, InvalidTokenError) as e:
        return e
        