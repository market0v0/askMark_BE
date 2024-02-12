# controller
from flask import jsonify, request
from App.model.userModel import User
import jwt
import datetime
import hashlib
from App.utils.encrypt import encrypt, decrypt

from mongoengine import Document
from App import db
import os

from App.utils.decoder import extract_payload, token_expired

class userController(Document):
    def create_user(self):  # Add 'self' as the first parameter
        try:
            data = request.get_json()
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            if not username or not email or not password:
                return jsonify({"error": "Missing required data"}), 400

            user = User(username=username, email=email, password=password)

            user.save()

            return jsonify(
                {
                    "message": "User created successfully",
                }
            )
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def login_user(self):
        key = os.getenv("SECRET_KEY")
        try:
            data = request.get_json()
            username = data.get("username")
            password = data.get("password")

            if not username or not password:
                return jsonify({"error": "Missing required data"}), 400

            user = db.user.find_one({"username": username})

            if user is None or user["password"] != password:
                return jsonify({"error": "User not found"}), 404

            payload = {
                "username": user["username"],
            }

            token = jwt.encode(payload, key, algorithm="HS256")
            mtoken = encrypt(token)
            return (

                jsonify(
                    {
                        "token": mtoken,
                    }
                ),
                200,
            )
        except Exception as e:
            return (jsonify({"error": str(e)}),)

    def create_link(self):
        try:
            mtoken = request.headers.get("Authorization")
            token = decrypt(mtoken)
            username = extract_payload(token).get("username")

            user = db.user.find_one({"username": username})
            if user is None:
                return jsonify({"error": "User not found"}), 404

            link_id = user.get("_id") 
            return jsonify({"link": str(link_id)}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def logout(self):
        try:
            mtoken = request.headers.get("Authorization")
            token = decrypt(mtoken)
            
          

        except Exception as e:
            return jsonify({"error": str(e)}), 500


    def edit_user(self):
        try:
            data = request.get_json()
            newusername = data.get("newusername")
            newemail = data.get("newemail")
            newpassword = data.get("newpassword")
            mtoken = request.headers.get("Authorization")
            token = decrypt(mtoken)
            username = extract_payload(token).get("username")
            user = db.user.find_one({"username": username})

            if user is None:
                return jsonify({"error": "User not found"}), 404

            db.user.update_one(
                {"username": username},
                {
                    "$set": {
                        "username": newusername,
                        "email": newemail,
                        "password": newpassword,
                    }
                },
            )
            return jsonify({"username": newusername}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500
