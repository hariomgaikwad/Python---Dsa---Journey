# Exercise 8: User class with password validation

# Logic
# __init__() stores username and password.
# check_password() compares the entered password with the stored password.
# Returns:
# True → if passwords match
# False → otherwise

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, input_password):
        return self.password == input_password


u1 = User("alice", "secure123")

print(u1.check_password("secure123"))
print(u1.check_password("password123"))