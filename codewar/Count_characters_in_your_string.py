# The main idea is to count all the occurring characters in a string.
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

def count(string):
    # The function code should be here
    string_list = list(string)
    res = {}
    for char in string_list:
        res[char] = string.count(char)

    print(res)


count("hello")
count("How are u? I'm fine, and u?")
