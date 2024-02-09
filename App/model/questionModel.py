from mongoengine import Document, StringField, DateTimeField, ReferenceField, CASCADE, BooleanField
from datetime import datetime
from App.model.userModel import User

class Question(Document):
    user = ReferenceField(User, reverse_delete_rule=CASCADE, reverse_save_rule=CASCADE)
    question = StringField(required=True)
    answer = StringField(required=True)
    createdDate = DateTimeField(default=datetime.now, required=True)  
    status = BooleanField(default=False, required=True)