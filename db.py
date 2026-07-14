from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["expenceTracker_db"]

expence_tracker = db["expence_tracker"]