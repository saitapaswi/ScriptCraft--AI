import bcrypt
from db import users_col

def signup_user(name, email, password):
    if users_col.find_one({"email": email}):
        return "User already exists"

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    users_col.insert_one({
        "name": name,
        "email": email,
        "password": hashed
    })

    return "Signup successful"

def login_user(email, password):
    user = users_col.find_one({"email": email})

    if not user:
        return None

    if bcrypt.checkpw(password.encode(), user["password"]):
        return user

    return None