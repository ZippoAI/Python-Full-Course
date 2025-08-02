import json
import os
import hashlib

USER_DB = "users.json"

def load_users():
    if not os.path.exists(USER_DB):
        return {}
    with open(USER_DB, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_DB, "w") as f:
        json.dump(users, f)

def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def register():
    users = load_users()
    username = input("Choose a username: ").strip()
    if username in users:
        print("That username already exists. Try logging in.")
        return
    pw1 = input("Enter your password: ")
    pw2 = input("Enter your password again: ")
    while pw1 != pw2:
        print("Passwords do not match.")
        pw2 = input("Enter your password again: ")
    users[username] = hash_password(pw1)
    save_users(users)
    print("Registration successful. You can now log in.")

def login():
    users = load_users()
    username = input("Enter your username: ").strip()
    if username not in users:
        print("No such user. Please register first.")
        return
    password = input("Enter your password: ")
    if hash_password(password) == users[username]:
        print("Login successful")
    else:
        print("You entered the wrong pass")

def main():
    while True:
        choice = input("Type 'register' to create account or 'login' to sign in (or 'exit' to quit): ").strip().lower()
        if choice == "register":
            register()
        elif choice == "login":
            login()
        elif choice == "exit":
            print("Goodbye.")
            break
        else:
            print("Unknown option. Please type 'register', 'login', or 'exit'.")

if __name__ == "__main__":
    main()
