# Task Overview:
#
# You have to write a function that accepts three parameters:
#
# cap is the amount of people the bus can hold excluding the driver.
# on is the number of people on the bus excluding the driver.
# wait is the number of people waiting to get on to the bus excluding the driver.
# If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.

def enough(cap, on, wait):
    all_people = on + wait
    return 0 if all_people < cap else all_people - cap


print(enough(100, 20, 50))
print(enough(70, 60, 20))
print(enough(80, 60, 10))