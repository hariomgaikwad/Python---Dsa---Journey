# Exercise 7: Access 'history' key

# logic
# Access outer key → student["grades"]
# Then inner key → ["history"]

student = {
    "name": "Hariom",
    "grades": {
        "math": 88,
        "science": 92,
        "history": 75
    }
}

print("History grade:", student["grades"]["history"])