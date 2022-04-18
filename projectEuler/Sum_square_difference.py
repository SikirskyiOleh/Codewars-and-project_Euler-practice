# Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.

sum1, sum2 = 0, 0

for i in range(1, 101):
    sum1 += i * i

for i in range(1, 101):
    sum2 += i

sum2 *= sum2

print(sum2 - sum1)
