from flask import Flask, jsonify
import requests

app = Flask(__name__)

def discover(service_name):
    res = requests.get(f"http://consul:8500/v1/catalog/service/{service_name}")
    data = res.json()
    if not data:
        return None, None
    return data[0]["ServiceAddress"], data[0]["ServicePort"]

@app.route("/<service>/info")
def proxy(service):
    address, port = discover(f"service-{service}")
    if not address:
        return jsonify(error="Service not found"), 404
    resp = requests.get(f"http://{address}:{port}/info")
    return resp.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
