from mongoengine import (
    Document,
    StringField,
    EmailField,
    DateTimeField,
    ReferenceField,
    CASCADE,
)


class User(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
