import configparser
import csv
import io
import os

from bson.json_util import dumps, loads
from flask import Flask, jsonify, render_template, request, Response
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

@app.route('/ducks/csv', methods=['GET'])
def export_ducks_to_csv():
    app.logger.debug("Exporting ducks to CSV")
    # Prepare CSV output
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write CSV headers
    writer.writerow(['Name', 'Color', 'Size', 'Rarity'])

    # Fetch all ducks from the database
    ducks = list(ducks_collection.find())
    
    # Write duck data to the CSV
    for duck in ducks:
        writer.writerow([duck.get('name'), duck.get('color'), duck.get('size'), duck.get('rarity')])

    # Set the response headers for CSV download
    response = Response(output.getvalue(), mimetype='text/csv')
    response.headers["Content-Disposition"] = "attachment; filename=ducks.csv"
    return response


if __name__ == "__main__":
    # Get the port number from the config
    port = config.getint("server", "port")
    app.run(host="0.0.0.0", debug=True, port=port)
