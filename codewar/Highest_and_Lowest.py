# In this little assignment you are given a string of
# space separated numbers, and have to return the highest and lowest number.

def high_and_low(numbers):
    lst = numbers.split(' ')
    lst = [int(i) for i in lst]
    minN = min(lst)
    maxN = max(lst)
    numbers = f'{str(maxN)} {str(minN)}'
    return numbers


high_and_low('1 2 3 4')
