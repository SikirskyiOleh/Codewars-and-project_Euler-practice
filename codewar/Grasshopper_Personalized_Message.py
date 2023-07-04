# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"


print(greet("Max", "Max"))
print(greet("Max", "Daniel"))
print(greet("Greg", "Greg"))
