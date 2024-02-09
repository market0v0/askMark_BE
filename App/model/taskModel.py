from mongoengine import Document, StringField, DateTimeField, ReferenceField, CASCADE
from datetime import datetime
from App.model.userModel import User

class Task(Document):
    name = StringField(required=True, unique=True)
    user = ReferenceField(User, reverse_delete_rule=CASCADE, reverse_save_rule=CASCADE)
    content = StringField(required=True)
    duedate = DateTimeField(default=datetime.now, required=True)  # Use required=True
    taskType = StringField(required=True)
