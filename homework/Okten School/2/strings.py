# strings

# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі


# 1)

# input_str = list(input("Enter your str: "))
# [print(x, end=',') for x in input_str if x.isdigit() == True]

# 2)

# import re
# input_str = input("Enter your str: ")
# new_list = list(map(int, re.findall(r'\d+', input_str)))
# print(new_list)