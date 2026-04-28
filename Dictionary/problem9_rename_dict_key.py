# Exercise 9: Rename key in dictionary

# logic
# pop("fname") → remove old key & get value
# Assign value to new key → "first_name"

employee = {"fname": "John", "age": 30, "dept": "Engineering"}

# rename key
employee["first_name"] = employee.pop("fname")

print(employee)