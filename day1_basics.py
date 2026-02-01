"""Day 1: Variables and data types"""

name = "Aditya"
age = 29
is_engineer = True

print("Name:", name)
print("Age:", age)
print("Engineer:", is_engineer)

print(type(name))
print(type(age))
print(type(is_engineer))

"""Basic login security check"""

username = "Aditya"
failed_attempts = 2

if failed_attempts >= 3:
    print(f"User {username} is locked.")
else:
    print(f"User {username} is allowed.")

"""Login risk level check"""

username = "Aditya"
failed_attempts = 2

if failed_attempts < 0:
    print("Invalid failed attempts count")
elif failed_attempts == 0:
    print(f"User {username} has no failed attempts.")
elif failed_attempts in (1, 2):
    print(f"User {username} is safe.")
else:
    print(f"User {username} is locked.")

"""Processing multiple users"""

users = ["admin", "john", "alice"]

for user in users:
    print(f"Checking user: {user}")

users = [
    {"username": "admin", "failed_attempts": 5},
    {"username": "john", "failed_attempts": 1},
    {"username": "alice", "failed_attempts": 0}
]

for user in users:
    if user["failed_attempts"] >= 3:
        print(f"User {user['username']} is locked")
    else:
        print(f"User {user['username']} is allowed")
