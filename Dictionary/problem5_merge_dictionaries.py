# Exercise 5: Merge dictionaries

# logic
# Copy first dictionary
# Use update() to merge second
# Common keys → second dictionary value overrides

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

result = dict1.copy()
result.update(dict2)

print(result)