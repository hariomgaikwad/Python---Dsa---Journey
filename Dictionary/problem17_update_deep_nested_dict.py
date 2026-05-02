# Exercise 17: Update deeply nested value

# logic
# Traverse each level using keys
# Update final key value

data = {
    "school": {
        "department": {
            "class": {
                "teacher": "Mr. Smith",
                "students": 30
            }
        }
    }
}

# update students
data["school"]["department"]["class"]["students"] = 35

print(data)