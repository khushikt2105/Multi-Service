from flask import Flask, jsonify
import requests, socket, time

app = Flask(__name__)

@app.route("/info")
def info():
    return jsonify(service="Service C", timestamp=time.time())

def register():
    time.sleep(3)
    payload = {
        "ID": "service-c",
        "Name": "service-c",
        "Address": socket.gethostbyname(socket.gethostname()),
        "Port": 5003,
        "Check": {
            "HTTP": f"http://{socket.gethostbyname(socket.gethostname())}:5003/info",
            "Interval": "10s"
        }
    }
    requests.put("http://consul:8500/v1/agent/service/register", json=payload)

if __name__ == "__main__":
    register()
    app.run(host="0.0.0.0", port=5003)
