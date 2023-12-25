# 1)Створити пустий list
# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 5) при створені об'єкта __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text

emptyList = []


class Letter:
    __count = 0  # initialise count to zero

    def __init__(self, text: str):
        self.__text = text
        Letter.__count += 1  # increment count by one for each new instance

    @classmethod
    def get_count(cls):
        return cls.__count

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        self.__text = new_text

    def __delete_text(self):
        del self.__text

    text = property(fget=__get_text, fset=__set_text, fdel=__delete_text)


def writeText(empty_list, some_text):
    empty_list.append(some_text)


someLetter = Letter('Something')
print(someLetter.get_count())
someLetter.text = 'Something new'
print(someLetter.text)

writeText(emptyList, someLetter.text)
print(emptyList)
