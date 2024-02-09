# __init__.py
from flask_cors import CORS
import os
from dotenv import load_dotenv
from flask import Flask
from flask_pymongo import PyMongo

# Load environment variables from .env
load_dotenv()

from mongoengine import connect

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
CORS(app)
# Connect to the MongoDB database using the MONGO_URI
connect(host=app.config["MONGO_URI"])

mongodb_client = PyMongo(app)
db = mongodb_client.db

from App import routes
