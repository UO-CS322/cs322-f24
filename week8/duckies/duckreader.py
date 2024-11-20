from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client["duckdb"]
ducks_collection = db["ducks"]

print(ducks_collection.find_one({"rarity": "rare"}))