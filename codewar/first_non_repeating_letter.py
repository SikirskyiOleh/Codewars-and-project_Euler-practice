# Best practice
# def first_non_repeating_letter(string):
#     list = [i.lower() for i in string]
#     for i in range(len(list)):
#         if list.count(list[i]) == 1:
#             return string[i]
#     return ""


def first_non_repeating_letter(string):
    word_list_or = list(string)
    word_list = list(string.lower())

    for i in word_list:
        if string.count(i) == 1:
            smt = word_list_or.index(i)
            print(word_list_or[smt])


first_non_repeating_letter('Hello')
first_non_repeating_letter("'~><#~><'")
first_non_repeating_letter('hello world, eh?')
first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!')
