import random

chars = "~`!@#$%^&*()_-+={[}\\]|:;\"'<,>.?/ABCDEFGHIKLMNOPQRSTVXYZabcdefghijklmnopqrstuvwxyz1234567890"

numberOfPasswords = int(input("Input number of passwords"))

lengthOfPasswords = int(input("Input length of passwords"))

for char in range(numberOfPasswords):
    password = ''
    for length in range(lengthOfPasswords):
        password += random.choice(chars)

