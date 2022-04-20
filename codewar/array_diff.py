def array_diff(a, b):
    # your code here
    lst = [x for x in a if x not in b]
    print(lst)


array_diff([1, 2, 3], [1])
