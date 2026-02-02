import re

def check_password_strength(password):
    strength = "Weak"

    # BUG 1: Length condition wrong (should be >= 8)
    if len(password) > 8:
        strength = "Medium"

    # BUG 2: Uppercase check incorrect
    if re.search("[A-Z]", password) == None:
        strength = "Strong"

    # BUG 3: Number check reversed
    if re.search("[0-9]", password) == None:
        strength = "Strong"

    # BUG 4: Special character not checked properly
    if re.search("[!@#$%^&*]", password):
        strength = "Weak"

    return strength


pwd = input("Enter your password: ")
print("Password Strength:", check_password_strength(pwd))
