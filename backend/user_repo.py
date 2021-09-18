from database import repo

class UserRepo:
    def __init__(self):
        self.db = repo("user")
    
    def authenticate(self, username, password):
        entry = self.db.get_entry("username", username)
        if entry != None:
            if entry["username"] == username and entry["password"] == password:
                return entry
        return False

    def read_user(self, id):
        return self.read(id)

    # data = json object
    # default values: {"username":"yourstring", "password":"yourstring"}
    def create_user(self, data):
        return self.create(data)

    # data = json object
    def update_info(self, id, data):
        return self.db.update(id, data)
        