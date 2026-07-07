# Exercise 9: Temperature class

# Logic 
# __init__() stores the temperature in Celsius.
# to_fahrenheit() uses the formula:
# (C × 9/5) + 32
# to_kelvin() uses the formula:
# C + 273.15
# Both methods return the converted temperature.

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15


t = Temperature(100)

print("Celsius:", t.celsius)
print("Fahrenheit:", t.to_fahrenheit())
print("Kelvin:", t.to_kelvin())