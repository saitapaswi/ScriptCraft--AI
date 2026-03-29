from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["scriptcraft"]

users_col = db["users"]
content_col = db["content"]