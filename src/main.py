from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/register", methods=["POST"])
def user_create():
    return "POST function"

@app.route("/<int:id>", methods=["GET"])
def user_profile(id):
    return "GET function"

@app.route("/<int:id>", methods=["PUT"])
def user_update(id):
    return "PUT function"

@app.route("/<int:id>", methods=["DELETE"])
def user_delete(id):
    return "DELETE function"
