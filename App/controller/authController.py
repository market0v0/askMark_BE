from flask import jsonify, request
import jwt
import os
from functools import wraps
from mongoengine import Document
from App.model.userModel import User
from App import db
from App.utils.encrypt import encrypt, decrypt

class AuthController(Document):
    def token_required(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            mtoken = request.headers.get("Authorization")
            if not mtoken:
                return jsonify({"valid": False}), 401
            token = decrypt(mtoken)
            key = os.getenv("SECRET_KEY")
            try:
                data = jwt.decode(token, key, algorithms="HS256")
            except jwt.ExpiredSignatureError:
                return jsonify({"valid": False}), 401
            except jwt.InvalidTokenError:
                return jsonify({"valid": False}), 401

            return jsonify({"data": data,"valid": True }), 200

        return decorated
