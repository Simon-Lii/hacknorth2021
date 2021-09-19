from . import authentication, bucket, music_trans
from .user_repo import UserRepo
import os
from werkzeug.utils import secure_filename
from flask import Flask, make_response, request, jsonify
import uuid
import json

db_user = UserRepo()

app = Flask("app")
if not os.path.exists('../uploads'):
    os.makedirs("../uploads")

def retrieve_id(token):
    return authentication.verify_data(token)[1]


@app.route("/api/delete_user/", methods=["POST"])
def delete_user():
    if "username" in request.form and "password" in request.form:
        username, password = request.form["username"], request.form["password"]
        if db_user.authenticate(username, password):
            db_user.delete_user(username)
            return {"status": "success"}, 200
        else:
            return {"status": "unauthorized"}, 401
    else:
        return {"status": "bad request"}, 400


@app.route("/api/create_user/", methods=["POST"])
def make_user():
    if "username" in request.form and "password" in request.form:
        username, password = request.form["username"], request.form["password"]
        if db_user.check_user(username):
            db_user.create_user(username, password)
            return jsonify({"status": "success"}), 200
        else:
            return jsonify({"status": "user already exists"}), 401
    else:
        return jsonify({"status": "bad request"}, 400)


@app.route("/api/auth/")
def auth_check():
    if "token" not in request.cookies:
        return jsonify({"status": "bad request"}), 400
    id = authentication.verify_data(request.cookies["token"])
    if id[1]:
        return jsonify({"status": "authenticated"}), 200
    return jsonify({"status": "authenticated"}), 200


@app.route("/api/login/", methods=["POST"])
def login():
    if "username" in request.form and "password" in request.form:
        username, password = request.form["username"], request.form["password"]
        auth_val = db_user.authenticate(username, password)
        if auth_val:
            token_val = authentication.get_token(auth_val)
            print(token_val)
            response = make_response(jsonify({"status": "success"}))
            response.set_cookie("token", token_val, httponly=True)
            return response
        else:
            return {"status": "invalid user"}, 401
    else:
        return {"response": "bad request"}, 400

# {"username":"something"}
@app.route("/api/upload", methods=["POST"])
def upload_api():
    token = request.cookies["token"]
    id = retrieve_id(token)
    if "file" in request.files:
        saved_file = request.files["file"]
        saved_file.save(os.path.join("audio_transcription/temp_song/", secure_filename(saved_file.filename)))
        data = music_trans.audio_to_score(saved_file.filename)
        pdf_filename = data[1]
        musical_data = data[2]
        entry = db_user.read_user(id)
        new_history_field = {"history": entry["history"] + [musical_data]}
        db_user.update_user(id, new_history_field)
        return {"status": "success", "filename": bucket.generate_presigned_url(pdf_filename)}, 200
    return {"status": "bad request"}, 400


@app.route("/api/sign_out", methods=["GET"])
def sign_out():
    resp = make_response()
    resp.set_cookie("token", "", expires=0)
    return resp

@app.route("/api/history", methods=["GET"])
def get_history():
    resp = make_response()
    token = request.cookies["token"]
    id = retrieve_id(token)
    entry = db_user.read_user(id)
    history = entry["history"]
    resp = []
    for h in history:
        pdf_filename = h[0].removesuffix('.wav') + ".pdf"
        temp_resp = {"title": h[0].removesuffix('.wav'), "url" : bucket.generate_presigned_url(pdf_filename)}
        resp.append(temp_resp)
    return {"body": resp}, 200
