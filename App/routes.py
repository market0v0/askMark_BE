# routes
from App import app
from flask import jsonify
import os
from App.controller.userController import userController
from App.controller.authController import AuthController
from App.controller.questionController import questionController
from App.controller.taskController import taskController
import jwt
from functools import wraps


@app.route("/")
def index():
    return "hello"


@app.route("/add")
def test():
    return jsonify("mark:" "mark")


@app.route("/create_user", methods=["POST"])
def create_user_route():
    return userController().create_user()


@app.route("/login_user", methods=["POST"])
def login_user_route():
    return userController().login_user()


@app.route("/getData", methods=["GET"])
@AuthController.token_required
def protected_resource():
    return jsonify({"message": "This is a protected resource"})


@app.route("/edit", methods=["PUT"])
def edit_user():
    return userController().edit_user()


@app.route("/create_task", methods=["POST"])
def create_task_route():
    return taskController().create_task()

@app.route("/ask", methods=["POST"])
def ask_route():
    return questionController().ask_question()

@app.route("/generate_link", methods=["GET"])
def generate_link():
    return userController().create_link()

@app.route("/logout", methods=["GET"])
def logout():
    return userController().logout()

@app.route("/answer", methods=["PUT"])
def answer():
    return questionController().answer_question()

@app.route("/questions", methods=["GET"])
def questions():
    return questionController().get_questions()