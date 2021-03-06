from flask import Flask
from AdbApi import adb_api
from OfonoApi import ofono_api
from BluezApi import bluez_api

app = Flask(__name__)

app.register_blueprint(adb_api, url_prefix='/adb')
app.register_blueprint(ofono_api, url_prefix='/ofono')
app.register_blueprint(bluez_api, url_prefix='/bluetooth')

@app.route("/")
def hello():
    return "Hello! Nothing here yet..."

if __name__ == "__main__":
    app.run(host="0.0.0.0")
