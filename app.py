from flask import Flask, render_template

app = Flask(__name__)
from flask_cors import CORS, cross_origin

CORS(app, resources={r"/": {"origins": "https://example.com"}})


@app.route("/")
def home():
    return render_template("index.html")


@cross_origin
@app.route("/map")
def map():
    return render_template("map.html")


if __name__ == "__main__":
    app.run()
