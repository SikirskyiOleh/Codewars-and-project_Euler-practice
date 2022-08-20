# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

def simple_multiplication(number):
    # Your code goes here
    return number * 8 if number % 2 == 0 else number * 9


case = simple_multiplication(5)
print(case)
