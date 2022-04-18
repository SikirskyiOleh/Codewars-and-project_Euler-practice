# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 6008514, являющийся простым числом?

n = 6008514
lis = []
lisN = []
for i in range(2, n):
    if n % i == 0:
        lis.append(i)

for i in lis:
    for j in range(2, int(i / 2) + 1):
        if (i % j) == 0:
            break
    else:
        lisN.append(i)

print(lis)
m = max(lisN)
print(m)
