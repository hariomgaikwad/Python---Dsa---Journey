# Exercise 7: Light class with ON/OFF state

# Logic
# is_on stores the current state of the light.
# turn_on() changes the state to True.
# turn_off() changes the state to False.
# status() checks the state and displays whether the light is ON or OFF.

class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Light is ON")

    def turn_off(self):
        self.is_on = False
        print("Light is OFF")

    def status(self):
        if self.is_on:
            print("Current status: ON")
        else:
            print("Current status: OFF")


light = Light()

light.turn_on()
light.status()

light.turn_off()
light.status()