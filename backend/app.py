from database import repo
from flask import Flask
from flask import request
import authentication

db_user = repo("user_db")
mongo_id = "614555ee4118c7e524b4948b"

app = Flask("app")

@app.route("/api/login", methods=["POST"])
def login():
    if "username" in request.form and "password" in request.form:
        username, password = request.form["username"], request.form["password"]
        auth_val = db_user.authenticate(username, password)
        if auth_val:
            token_val = authentication.get_token(username)
            response = make_response()






@app.route("/api/upload", methods=["POST"])
def upload_api():
    if 'file' not in request.files:
