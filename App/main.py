from flask import Blueprint
from .extensions import mongo

main = Blueprint('main', __name__)



@main.route('/')
def home():
    user_collection = mongo.db.users
    user_collection.insert({'name' : 'mark'})
    return "mark"


    

