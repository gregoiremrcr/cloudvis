from pymongo import MongoClient
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(mongo_uri)

db = client["cloudvision"]
collection = db["analyses"]

def insert_analysis(data):
    data["timestamp"] = datetime.utcnow()
    result = collection.insert_one(data)
    return str(result.inserted_id)

def get_all_analyses():
    return list(collection.find().sort("timestamp", -1))
