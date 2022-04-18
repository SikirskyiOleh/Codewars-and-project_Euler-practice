# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?

from itertools import count

for i in count(20):
    if all(map(lambda x: i % x == 0, range(1, 21))):
        print(i)
        break
