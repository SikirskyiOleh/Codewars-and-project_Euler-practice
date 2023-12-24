# 1) створити два класи Prince і Cinderella:
# в Cinderella повинне бути імя вік і розмір ноги
# в Prince імя, вік і розмір знайденої туфельки, так же повинен бути метод який приймає лист Cinderella та шукає ту саму
#
# 2) максимально в цих двох класах проанотировати типи
#
# 3) в класі Cinderella повинна бути змінна count яка буде рахувати скільки екземплярів класу Cinderella було створено

class Cinderella:
    __count = 0  # initialise count to zero

    def __init__(self, name: str, age: int, foot_size: int):
        self._name = name
        self._age = age
        self._foot_size = foot_size
        Cinderella.__count += 1  # increment count by one for each new instance

    def __str__(self):
        return f'Cinderella({self._name} - {self._age} - {self._foot_size})'

    def __repr__(self):
        return f'Cinderella({self._name} - {self._age} - {self._foot_size})'

    @classmethod
    def get_count(cls):
        return cls.__count

    def get_foot_size(self):
        return self._foot_size


class Prince:
    def __init__(self, name: str, age: int, shoe_size: int):
        self._name = name
        self._age = age
        self._shoe_size = shoe_size

    def __str__(self):
        return f'Prince({self._name} - {self._age} - {self._shoe_size})'

    def __repr__(self):
        return f'Prince({self._name} - {self._age} - {self._shoe_size})'

    def findCinderella(self, listCinderellas: list[Cinderella]):
        for cinderella in listCinderellas:
            if self._shoe_size == cinderella.get_foot_size():
                print(cinderella.__repr__())
                return
            else:
                print('Cinderella not found')


cinderellas_list: list[Cinderella] = [
    Cinderella('Kira', 25, 34),
    Cinderella('Karina', 18, 32),
    Cinderella('Kamila', 16, 31),
    Cinderella('Olha', 22, 35),
    Cinderella('Toma', 21, 38),
]

print(f'Cinderellas instance created:{Cinderella.get_count()}')

prince = Prince('Max', 27, 35)

prince.findCinderella(cinderellas_list)
