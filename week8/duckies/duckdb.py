from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client["duckdb"]
ducks_collection = db["ducks"]

duck1 = {"name": "Duckie", "color": "yellow", "size": "small", "rarity": "common"}

duck2 = {"name": "Duckie Jr.", "color": "blue", "size": "small", "rarity": "rare"}

result = ducks_collection.insert_many([duck1, duck2])
