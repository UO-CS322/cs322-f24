# pylint: disable=unused-argument
"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import logging

import arrow
import flask
from flask import request

import acp_times  # Brevet time calculations
import config

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY
# error
ERROR = 0.2
###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    """Redirect to the main brevet calculator page."""
    app.logger.debug("Main page entry")
    return flask.render_template("calc.html")


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    app.logger.debug("Page not found")
    flask.session["linkback"] = flask.url_for("index")
    return flask.render_template("404.html"), 404


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
        return flask.jsonify(result=result)

    open_close = {"open": open_time, "close": close_time}
    app.logger.debug(f"result: {open_close}")
    return flask.jsonify(result=open_close)


#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    app.logger.debug(f"Opening for global access on port {CONFIG.PORT}")
    app.logger.setLevel(logging.DEBUG)
    app.run(port=CONFIG.PORT, host="0.0.0.0", debug=True)
