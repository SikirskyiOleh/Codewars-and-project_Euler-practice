# list comprehension

# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ в ліст поміняв його на верхній регістр
# приклад:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
#
# 2) з діапазона від 0-50 записати в ліст тілько не парні числа, при цьому підняти їх в квадрат
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]


# 1)

# greeting = 'Hello, world'
# new_lst = [i.upper() for i in list(greeting)]
# print(new_lst)

# 2)

# lst = [i**2 for i in range(0,50) if i % 2 == 0]
# print(lst)