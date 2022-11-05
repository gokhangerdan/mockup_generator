from flask import Flask, request
import json

app = Flask(__name__)
app.config["mockup_file"] = "mockup_file"

with open("{}.json".format(app.config["mockup_file"]), "r") as f:
    mockup_data = json.load(f)

@app.route("/<name>", methods=['GET', 'POST'])
def hello_world(name):
    name = "/{}".format(name)
    for i in mockup_data:
        if (name==i["url"]) and (request.method==i["method"]):
            return i["body"], i["status"]
