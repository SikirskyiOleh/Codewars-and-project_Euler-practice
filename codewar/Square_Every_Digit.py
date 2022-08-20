# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

def square_digits(num):
    tpmList = [int(x) for x in str(num)]
    resultList = []
    for i in tpmList:
        resultList.append(i * i)
    tmp = [str(integer) for integer in resultList]
    result = int("".join(tmp))
    return result


case = square_digits(123)
print(case)
