from flask import abort, Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello_world():
    return jsonify(message="Hello, World!")


# Serve pages
@app.route("/<path:file>")
def serve_page(file):
    try:
        return render_template(file), 200
    except Exception as e:
        return abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6006)
