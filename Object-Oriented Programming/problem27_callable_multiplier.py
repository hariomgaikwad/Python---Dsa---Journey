# Exercise 27: Callable object using __call__

# Logic
# factor is stored when the object is created.
# __call__() makes the object behave like a function.
# Calling multiply_by_3(10) automatically executes multiply_by_3.__call__(10).
    
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return self.factor * number


multiply_by_3 = Multiplier(3)
multiply_by_5 = Multiplier(5)

print(multiply_by_3(10))
print(multiply_by_5(7))