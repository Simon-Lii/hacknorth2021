from database import repo
from user_repo import UserRepo
from flask import Flask

db_user = UserRepo()
print(db_user.authenticate("admin","ADMIN"))

app = Flask("app")

@app.route("/")
def hello_world():
    return "<p>Hi</p>"