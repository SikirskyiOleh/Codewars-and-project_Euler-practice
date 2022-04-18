# from collections import Counter
# def count(string):
#     return Counter(string)

def count(string):
    # The function code should be here
    string_list = list(string)
    res = {}
    for char in string_list:
        res[char] = string.count(char)

    print(res)


count("hello")
count("How are u? I'm fine, and u?")
