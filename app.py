from flask import Flask, render_template
import requests

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

@cross_origin
@app.route("/mapfetch")
def mapfetch():
    return render_template("mapFetch.html")


if __name__ == "__main__":
    app.run()
