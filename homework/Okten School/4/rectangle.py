# Створити клас Rectangle:
# -конструктор приймає дві сторони x,y
# -описати арифметичні методи
#   + сума площів двох екземплярів класа
#   - різниця площадів
#   == чи площі рівні
#   != не равні
#   >, < менше чи більше
#   при виклку метода len() порахувати суму сторін


class Rectangle:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __add__(self, other):
        return self._x * self._y + other._x * other._y

    def __sub__(self, other):
        return self._x * self._y - other._x * other._y

    def __eq__(self, other):
        return self._x * self._y == other._x * other._y

    def __ne__(self, other):
        return self._x * self._y != other._x * other._y

    def __gt__(self, other):
        return self._x * self._y > other._x * other._y

    def __lt__(self, other):
        return self._x * self._y < other._x * other._y

    def __len__(self):
        return self._x + self._y


first_rectangle = Rectangle(3, 5)
second_rectangle = Rectangle(4, 9)

add = first_rectangle.__add__(second_rectangle)
print(add)
sub = first_rectangle.__sub__(second_rectangle)
print(sub)
eq = first_rectangle.__eq__(second_rectangle)
print(eq)
ne = first_rectangle.__ne__(second_rectangle)
print(ne)
gt = first_rectangle.__gt__(second_rectangle)
print(gt)
lt = first_rectangle.__lt__(second_rectangle)
print(lt)
lenght = first_rectangle.__len__()
print(lenght)
