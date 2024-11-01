from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/count", methods=["POST"])
# def count_characters():
#     data = request.json
#     text = data.get("text", "")
#     character_count = len(text)
#     return jsonify({"count": character_count})


@app.route("/count")
def count_characters():
    text = request.args.get("text", "")
    character_count = len(text)
    return f"Character count: {character_count}"


if __name__ == "__main__":
    app.run(debug=True, port=7007)
