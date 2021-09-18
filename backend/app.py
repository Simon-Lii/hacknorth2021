from database import repo
from flask import Flask

db = repo("test")
mongo_id = "614555ee4118c7e524b4948b"
resp = db.read(mongo_id)
print(resp)