# Exercise 30: Character auto level-up

# Logic
# The character starts at Level 1 with 0 exp.
# gain_exp() adds experience points.
# If exp becomes 100 or more, the character:
# Levels up.
# Removes 100 exp.
# Keeps the remaining exp.

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.exp = 0
        self.level = 1

    def gain_exp(self, amount):
        self.exp += amount

        if self.exp >= 100:
            self.level += 1
            self.exp -= 100
            print(f"{self.name} gained {amount} exp. Level up! Now Level {self.level}. (Remaining exp: {self.exp})")
        else:
            print(f"{self.name} gained {amount} exp. (Total: {self.exp})")


player = Character("Aria", 100)

player.gain_exp(60)
player.gain_exp(60)