# Exercise 16: Extract file extension

# logic
# Split string using "."
# Take last part using [-1]

file_name = "report_final_v2.pdf"

extension = file_name.split(".")[-1]

print(extension)