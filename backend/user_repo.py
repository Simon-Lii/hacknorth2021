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
        