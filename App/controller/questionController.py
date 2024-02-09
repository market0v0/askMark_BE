from mongoengine import Document, StringField, DateTimeField
from App import db
from flask import jsonify, request
from App.model.userModel import User
from App.model.questionModel import Question
from datetime import datetime
from bson.objectid import ObjectId
from App.utils.encrypt import encrypt, decrypt
from App.utils.decoder import extract_payload
class Ask(Document):
    urlID = StringField(required=True)
    question = StringField(required=True)
    createdDate = DateTimeField(default=datetime.now)


class questionController(Document):
    def ask_question(self):
        try:
            data = request.get_json()
            urlID = data.get("url")
            question = data.get("question")
            if not question or not urlID:
                return jsonify({"error": "Question and URL are required"}), 400
            user = User.objects(id=urlID).first()
            if user is None:
                return jsonify({"error": "User not found"}), 404

            question = Question(
                user=urlID,  
                question=question,
                answer="",
                createdDate=datetime.now(),
                status=False
            )
            question.save()


            return jsonify(
                {
                    "question": question.question,
                    "status": False,
                    "createdDate": question.createdDate.strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def answer_question(self):
        try:
            data = request.get_json()
            qID = data.get("questionId")
            answer = data.get("answer")

            if not answer:
                return jsonify({"error": "Answer is required"}), 400

            question = Question.objects(id=qID).first()
            if question is None:
                return jsonify({"error": "Question not found"}), 404

            # Update the question with the provided answer and change status
            question.answer = answer
            question.status = True
            question.save()

            return jsonify({"answer": answer})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_questions(self):
        try:
            mtoken = request.headers.get("Authorization")
            token = decrypt(mtoken)
            username = extract_payload(token).get("username")
            if not username:
                return jsonify({"error": "Username is required"}), 400

            user = User.objects(username=username).first()
            if user is None:
                return jsonify({"error": "User not found"}), 404

            questions = Question.objects(user=user)

            question_list = [
                {
                    "questionId": str(question.id),
                    "question": question.question,
                    "answer": question.answer,
                    "createdDate": question.createdDate.strftime("%Y-%m-%d %H:%M:%S"),
                    "status": question.status
                }
                for question in questions
            ]

            return jsonify({"questions": question_list})

        except Exception as e:
            return jsonify({"error": str(e)}), 500