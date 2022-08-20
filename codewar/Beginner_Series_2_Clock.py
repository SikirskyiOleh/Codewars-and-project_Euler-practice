# Clock shows h hours, m minutes and s seconds after midnight.
# Your task is to write a function which returns the time since midnight in milliseconds.

def past(h, m, s):
    # Good Luck!
    if h < 0 or h > 23:
        return 'Wrong time'
    elif m < 0 or m > 59:
        return 'Wrong time'
    elif s < 0 or s > 59:
        return 'Wrong time'

    res = (h * 3600000) + (m * 60000) + (s * 1000)
    return res


# better practice (3600*h + 60*m + s) * 1000
case = past(2, 1, 1)
print(case)
