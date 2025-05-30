import configparser
import os
import random

from bson.json_util import dumps, loads
from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient


app = Flask(__name__)

# Load configuration
config = configparser.ConfigParser()
config.read("app.ini")

# Connect to MongoDB
mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017/DuckyCollection")
if mongo_uri:
    client = MongoClient(mongo_uri)
else:
    client = MongoClient("localhost", 27017)
db = client["duckdb"]
ducks_collection = db["DuckyCollection"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add_duck", methods=["POST"])
def add_duck():
    data = request.get_json()
    duck = {
        "name": data["name"],
        "color": data["color"],
        "size": data["size"],
        "rarity": data["rarity"],
    }
    result = ducks_collection.insert_one(duck)
    return jsonify({"message": "Duck added!", "id": str(result.inserted_id)}), 201


@app.route("/search_duck", methods=["GET"])
def search_duck():
    name = request.args.get("name")
    duck = ducks_collection.find_one({"name": name})
    print(dumps(duck))
    if duck:
        return jsonify(dumps(duck)), 200
    return jsonify({"message": "Duck not found."}), 404


@app.route("/display", methods=["POST"])
def display_ducks():
    ducks = list(ducks_collection.find())
    for duck in ducks:
        duck["_id"] = str(duck["_id"])
    app.logger.debug("DB: {}".format(ducks))
    return render_template("ducks.html", items=ducks)


if __name__ == "__main__":
    # Get the port number from the config
    port = config.getint("server", "port")
    app.run(host="0.0.0.0", debug=True, port=port)
