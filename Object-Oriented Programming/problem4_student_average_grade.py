# Exercise 4: Student class with average grade

# Logic
# __init__() stores name and marks
# marks is a list (instance attribute)
# average() calculates:
# sum(self.marks) → total marks
# len(self.marks) → number of subjects
# sum / len → average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)


s1 = Student("Alice", [85, 90, 78, 92, 88])

print(f"{s1.name}'s Average Grade: {s1.average()}")