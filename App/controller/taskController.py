from mongoengine import Document
from App import db
import os
from flask import jsonify, request
from App.model.userModel import User
from App.model.taskModel import Task
import jwt
import datetime

from datetime import datetime

class taskController(Document):
    def create_task(self):
        try:
            data = request.get_json()
            name = data.get("name")
            username = data.get("username")
            content = data.get("content")
            duedate = data.get("duedate")  
            taskType = data.get("taskType")
            

            if not name or not duedate or not taskType:
                return jsonify({"error": "Invalid request data"}), 400

            user = User.objects(username=username).first()

            if user is None:
                return jsonify({"error": "User not found"}), 404
            task = Task(
                name=name,
                user=str(user.id),
                content=content,
                duedate=datetime.strptime(duedate,"%Y-%m-%dT%H:%M:%S.%fZ"),
                taskType=taskType
            )
            task.save()

            return jsonify(
                {
                    "message": "Task created successfully",
                    "name": str(task.name),
                }
            )
        except Exception as e:
            return jsonify({"error": str(e)}), 500
