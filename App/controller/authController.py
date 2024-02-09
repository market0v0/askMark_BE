from flask import jsonify, request
import jwt
import os
from functools import wraps
from mongoengine import Document
from App.model.userModel import User
from App import db


class AuthController(Document):
    @staticmethod
    def token_required(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            key = os.getenv("SECRET_KEY")
            token = request.headers.get("Authorization")
            print(token)
            if not token:
                return jsonify({"message": "Token is missing"}), 401
            try:
                data = jwt.decode(token, key, algorithms="HS256")
            except jwt.ExpiredSignatureError:
                return jsonify({"message": "Token has expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"message": "Invalid token"}), 401

            return jsonify(data)

        return decorated
