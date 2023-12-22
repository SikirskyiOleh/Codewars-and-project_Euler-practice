# function

# - створити функцію яка виводить ліст
# - створити функцію яка приймає три числа та виводить та повертає найменьше.
# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# - створити функцію яка повертає найбільше число з ліста
# - створити функцію яка повертає найменьше число з ліста
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def output_lst(lst):
    print(lst)


def min_num(a, b, c):
    print(min(a, b, c))
    return min(a, b, c)


def max_num(a, b, c):
    print(max(a, b, c))
    return max(a, b, c)


def min_max_num(*args):
    print(max(args))
    return min(args)


def max_num_lst(lst):
    max_n = max(lst)
    return max(lst)


def min_num_lst(lst):
    min_n = min(lst)
    return min(lst)


def sum_lst(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum


def avr_lst(lst):
    sum = 0
    for i in lst:
        sum += i

    return sum / len(lst)


output_lst([1, 2, 3, 4])

min_num(1, 2, 3)

max_num(1, 2, 3)

min_max_num(1, 2, 3, 4, 5, 6, 7)

max_n = max_num_lst([1, 2, 3, 4, 5])
print(max_n)

min_n = min_num_lst([1, 2, 3, 4])
print(min_n)

sum = sum_lst([1, 2, 3, 4, 5])
print(sum)

avr = avr_lst([1, 2, 3, 4, 5])
print(avr)
