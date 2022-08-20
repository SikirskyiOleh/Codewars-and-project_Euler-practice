# Write a function that returns both the minimum and maximum number of the given list/array.

def min_max(lst):
    minNumber = min(lst)
    maxNumber = max(lst)
    result = [minNumber, maxNumber]
    return result


case = min_max([1])
print(case)

# Best practice return [min(lst), max(lst)]