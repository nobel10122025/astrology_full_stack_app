from mongoengine import Document, StringField

class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    name = StringField(required=True)
    email = StringField(required=True)