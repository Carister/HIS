import uuid
from storage import users

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
        }

# Add a new user
def add_user(username, password):
    if username not in users:
        users[username] = User(username, password)
        return True
    return False

# Validate login credentials
def validate_user(username, password):
    user = users.get(username)
    return user and user.password == password 
       
        
class Client:
    def __init__(self, name, age):
        self.id = str(uuid.uuid4())
        self.name = name
        self.age = age
        self.enrolled_programs = []

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "enrolled_programs": self.enrolled_programs
        }

class Program:
    def __init__(self, name):
        self.name = name
