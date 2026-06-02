import json

DB_FILE = "db.json"

class DataManager:
    def load(self):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"users": [], "restaurants": []}
            self.save(data)
            return data

    def save(self, data):
        with open(DB_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def get_user(self, username, password):
        data = self.load()
        for user in data.get("users", []):
            if (user.get("username") == username and 
                user.get("password") == password and 
                user.get("role") == "customer"):
                return user
        return None

    def get_restaurants(self):
        data = self.load()
        return data.get("restaurants", [])

    def add_restaurant(self, restaurant):
        data = self.load()
        # Using setdefault prevents KeyErrors if "restaurants" is somehow missing
        data.setdefault("restaurants", []).append(restaurant)
        self.save(data)

    def add_user(self, username, password, role):
        data = self.load()
        data.setdefault("users", []).append({
            "username": username, 
            "password": password, 
            "role": role
        })
        self.save(data)