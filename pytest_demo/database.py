from typing import List, Dict


class Database:
    def __init__(self, users = None):
        self.connected = False
        if users is None:
            self.data = {"users": []}
        else:
            self.data = {"users": users}

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

    def add_user(self, user_id, name):
        if not self.connected:
            raise Exception("Database not connected")
        self.data["users"].append({"id": user_id, "name": name})

    def get_users(self):
        if not self.connected:
            raise Exception("Database not connected")
        return self.data["users"]