import re

def check_password_strength(password):
    # Define the criteria for a strong password
    length_regex = re.compile(r'.{8,}')
    uppercase_regex = re.compile(r'[A-Z]')
    lowercase_regex = re.compile(r'[a-z]')
    number_regex = re.compile(r'[0-9]')
    special_char_regex = re.compile(r'[^a-zA-Z0-9]')

    # Check each criteria and provide feedback
    strength = 0
    if length_regex.search(password):
        strength += 1
    if uppercase_regex.search(password):
        strength += 1
    if lowercase_regex.search(password):
        strength += 1
    if number_regex.search(password):
        strength += 1
    if special_char_regex.search(password):
        strength += 1

    # Return the password's strength
    return strength

# Test the password complexity checker
password = input("Enter a password: ")
strength = check_password_strength(password)
print("Password strength out of 5:", strength)
