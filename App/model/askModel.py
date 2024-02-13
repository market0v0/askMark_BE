from mongoengine import Document, StringField, DateTimeField,ListField, ReferenceField, CASCADE, BooleanField
from datetime import datetime
from App.model.userModel import User

class ask(Document):
    user = ReferenceField(User, reverse_delete_rule=CASCADE, reverse_save_rule=CASCADE)
    ask = StringField(required=True)
    answers = ListField(StringField(required=True))
    createdDate = DateTimeField(default=datetime.now, required=True)  
    status = BooleanField(default=False, required=True)