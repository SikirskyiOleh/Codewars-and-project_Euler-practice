# -Має бути клас записника
# -А кожна маніпуляція над нею має бути методом класу
# -Всі дані зберігаємо у файл
#
#
# Реалізувати записну книжку покупок:
# - кожен запис повинен містити назву покупки та її ціну
# -зробити меню для роботи з записною книжкою:
# '1) Створити запис'
# '2) Список всіх записів'
# '3) Загальна сума всіх покупок'
# '4) Найдорожча покупка'
# '5) Пошук за назвою покупки'
# '9) Вихід

import json
from typing import TypedDict

Purchase = TypedDict('Purchase', {'name': str, 'price': int})


class Notebook:

    def __init__(self):
        self.__data: list[Purchase] = []
        self.__read_file()

    def __read_file(self):
        try:
            with open('DB.json') as file:
                self.__data = json.load(file)
        except (Exception,):
            pass

    def __write_file(self):
        try:
            with open('DB.json', 'w') as file:
                json.dump(self.__data, file)
        except Exception as err:
            print(err)

    def __create_record(self):
        tmp_name = str(input('Введіть назву продукту: '))
        tmp_price = int(input('Введіть ціну: '))
        self.__data.append({'name': tmp_name, 'price': tmp_price})
        self.__write_file()

    def __get_all(self):
        for item in self.__data:
            print(item)

    def __total_price(self):
        tmp_lst = [sub['price'] for sub in self.__data]
        total = sum(tmp_lst)
        print(f'Загальна вартіть всіх покупок становить: {total}')

    def __max_price(self):
        sorted_data = sorted(self.__data, key=lambda i: i['price'])

        if not sorted_data:
            print('list is empty')
            return

        print(f'Найдорожча покупка це: {sorted_data[-1]}')

    def __search(self):
        search = input('Введіть що потрібно знайти: ')
        for item in self.__data:
            for value in item.values():
                if search == str(value):
                    print(item)

    def menu(self):

        while True:
            print('1) Створити запис')
            print('2) Список всіх записів')
            print('3) Загальна сума всіх покупок')
            print('4) Найдорожча покупка')
            print('5) Пошук за назвою покупки')
            print('9) Вихід')

            choice = int(input('Виберіть один із варіантів: '))

            if choice == 1:
                self.__create_record()
            elif choice == 2:
                self.__get_all()
            elif choice == 3:
                self.__total_price()
            elif choice == 4:
                self.__max_price()
            elif choice == 5:
                self.__search()
            elif choice == 9:
                break


smt = Notebook()
smt.menu()
