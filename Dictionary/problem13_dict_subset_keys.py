# Exercise 13: Extract subset of keys

# logic
# Loop through required keys
# Create new dictionary using comprehension
# Keep only selected keys

user = {
    "id": 42,
    "username": "hari",
    "email": "hari@example.com",
    "password": "12345",
    "joined": "2026-04-20"
}

keys_needed = ["id", "username", "email"]

result = {key: user[key] for key in keys_needed}

print(result)