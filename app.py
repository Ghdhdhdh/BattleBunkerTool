from flask import Flask, render_template, make_response, request, Response
import requests

app = Flask(__name__)
# from flask_cors import CORS, cross_origin


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/map")
def map():
    resp = make_response(render_template("map.html"))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return resp



@app.route("/mapfetch")
def mapfetch():
    resp = make_response(render_template("mapFetch.html"))
    # return resp

    # resp = make_response(render_template("map.html"))
    resp.headers["Access-Control-Allow-Origin"] = "*"   # allow every origin
    return resp   

def add_cors(resp):
  resp.headers["Access-Control-Allow-Origin"] = "https://your-frontend.example"
  resp.headers["Vary"] = "Origin"
  resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
  resp.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
  # resp.headers["Access-Control-Allow-Credentials"] = "true"  # if needed
  return resp

@app.route("/proxy/<path:path>", methods=["GET","POST","PUT","DELETE","OPTIONS"])
def proxy(path):
  if request.method == "OPTIONS":
    return add_cors(Response(status=204))

  url = f"https://{path}"
  upstream = requests.request(
    request.method, url,
    headers={k:v for k,v in request.headers if k.lower() not in ["host","origin"]},
    data=request.get_data(),
  )
  resp = Response(upstream.content, upstream.status_code)
  for k,v in upstream.headers.items():
    if not k.lower().startswith("access-control-"):
      resp.headers[k] = v
  return add_cors(resp)
if __name__ == "__main__":
    app.run(port=80)
