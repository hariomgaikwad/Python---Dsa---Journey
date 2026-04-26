# Exercise 6: Access nested dictionary

# logic
# Access outer key → person["address"]
# Then inner key → ["city"]

person = {
    "name": "Carol",
    "address": {"city": "Paris", "zip": "75001"}
}

print("City:", person["address"]["city"])