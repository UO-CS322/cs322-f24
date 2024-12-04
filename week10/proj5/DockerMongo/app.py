from re import I
import arrow
import configparser
import logging
import os

from bson.json_util import dumps, loads
from flask import Flask, jsonify, redirect, render_template, request, url_for
from pymongo import MongoClient

import acp_times  # Brevet time calculations


###
# Globals
###
app = Flask(__name__)

# Load configuration (https://docs.python.org/3/library/configparser.html)
CONFIG = configparser.ConfigParser()
CONFIG.read("app.ini")


# Connect to MongoDB (update as needed)
mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
if mongo_uri:
    client = MongoClient(mongo_uri)
else:
    client = MongoClient("localhost", 27017)
db = client.brevetdb

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    """Redirect to the main brevet calculator page."""
    app.logger.debug("Main page entry")
    return render_template("calc.html")


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    app.logger.debug("Page not found")
    return render_template("404.html"), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    # Format: { km: km, begin_date: begin_date, begin_time: begin_time, distance: distance }
    dist_km = request.args.get("dist_km", -1, type=float)
    brevet_dist_km = request.args.get("distance", -1, type=int)
    begin_date = request.args.get("begin_date", "0000-00-00", type=str)
    begin_time = request.args.get("begin_time", "00:00", type=str)

    # Covert the start time to ISO 8601 format
    begin_ts = arrow.get(begin_date + " " + begin_time, "YYYY-MM-DD HH:mm").isoformat()

    app.logger.debug(
        f"request.args: {request.args}, dist_km={dist_km}, begin_ts={begin_ts}"
    )
    try:
        open_time = acp_times.open_time(dist_km, brevet_dist_km, begin_ts)
        close_time = acp_times.close_time(dist_km, brevet_dist_km, begin_ts)
    except ValueError as err:
        message = str(err)
        app.logger.debug(f"ValueError: {message}")
        result = {"error": message}
        return jsonify(result=result)

    open_close = {"open": open_time, "close": close_time}
    app.logger.debug(f"result: {open_close}")
    return jsonify(result=open_close)


@app.route("/_store_times", methods=["POST"])
def store_times():
    data = request.get_json()
    app.logger.debug(f"Data: {str(data)}")
    for item in data:
        item_doc = {
            "km": item["km"],
            "begin_date": item["begin_date"],
            "begin_time": item["begin_time"],
            "distance": item["distance"],
            "open": item["open"],
            "close": item["close"],
        }
        db.brevetdb.insert_one(item_doc)
    return jsonify({"message": "Times stored successfully!"}), 201


@app.route("/display_times")
def display_times():
    items = list(db.brevetdb.find())
    for item in items:
        item["_id"] = str(item["_id"])
    app.logger.debug(f"Items: {items}")
    return render_template("display_times.html", items=items)


#############

app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    app.logger.debug(f"Opening for global access on port {CONFIG['server']['port']}")
    app.run(port=CONFIG["server"]["port"], host="0.0.0.0", debug=True)
