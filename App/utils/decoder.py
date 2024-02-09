import jwt

def extract_payload(token):
    try:
        # Decode the token without verifying the signature
        payload = jwt.decode(token, options={"verify_signature": False})
        return payload
    except jwt.ExpiredSignatureError:
        # Handle the case where the token has expired
        print("Token has expired")
    except jwt.InvalidTokenError:
        # Handle the case where the token is invalid
        print("Invalid token")