def narcissistic(value):
    # Code away
    b = map(int, str(value))

    ble = len(str(value))
    sums = 0
    print(b)

    for i in b:
        sums += i ** ble

    if sums == value:
        print(True)
    else:
        print(False)


print(narcissistic(7))
print(narcissistic(371))
print(narcissistic(122))
print(narcissistic(4887))
