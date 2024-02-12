import jwt
from datetime import datetime, timedelta
import os

def extract_payload(token):
    try:
        # Decode the token without verifying the signature
        payload = jwt.decode(token, options={"verify_signature": False})
        return payload
    except jwt.ExpiredSignatureError:
        # Handle the case where the token has expired
        return "Invalid token"
    except jwt.InvalidTokenError:
        # Handle the case where the token is invalid
        return "Invalid token"


def token_expired(token):
    key = os.getenv("SECRET_KEY")
    print( token)
    try:
        decoded_token = jwt.decode(token, key, algorithms=['HS256'])
        print(decoded_token)
        decoded_token['exp'] = datetime.utcnow()
        updated_token = jwt.encode(decoded_token, key, algorithm='HS256')
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False