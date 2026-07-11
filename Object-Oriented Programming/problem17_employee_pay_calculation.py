# Exercise 17: Employee pay calculation using inheritance

# Logic
# Employee is the parent class and stores the employee's name.
# FullTimeEmployee calculates monthly pay:
# annual_salary ÷ 12
# PartTimeEmployee calculates pay:
# hourly_rate × hours_worked
# Both classes have the same method name calculate_pay(), but each uses its own formula.

class Employee:
    def __init__(self, name):
        self.name = name


class FullTimeEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.annual_salary = annual_salary

    def calculate_pay(self):
        return self.annual_salary / 12


class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked


full_time = FullTimeEmployee("Alice", 60000)
part_time = PartTimeEmployee("Bob", 500, 20)

print(f"{full_time.name}'s monthly pay:", full_time.calculate_pay())
print(f"{part_time.name}'s monthly pay:", part_time.calculate_pay())