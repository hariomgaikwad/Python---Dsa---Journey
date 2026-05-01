# Exercise 16: Modify value in nested dictionary

# logic
# Access nested dictionary → company["location"]
# Update key → ["city"] = "Munich"

company = {
    "name": "TechCorp",
    "location": {"city": "Berlin", "country": "Germany"}
}

# update city
company["location"]["city"] = "Munich"

print(company)