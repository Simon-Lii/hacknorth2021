from pymongo import MongoClient
from bson.objectid import ObjectId


class repo:
    def __init__(self, collection):
        url = "mongodb+srv://simon:simon@hackthenorth2021.kat9o.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE"
        self.db = MongoClient(url, connect=False)["hack"][collection]

    def read(self, id):
        resp = self.db.find_one({"_id": ObjectId(id)})
        return resp

    def create(self, data):
        resp = self.db.insert_one(data)
        if resp.inserted_id:
            return self.read(resp.inserted_id)
        else:
            return None

    def update(self, id, data):
        resp = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return self.read(id)

    def delete_entry(self, field, value):
        resp = self.db.delete_one({field: value})
        return resp

    def get_entry(self, field, value):
        resp = self.db.find_one({field: value})
        return resp
