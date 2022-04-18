# Best practice
# def anagrams(word, words):
#   return [item for item in words if sorted(item)==sorted(word)]

def anagrams(word, words):
    lst = []
    word_list = list(word)
    word_list.sort()

    for i in words:
        words_list = list(i)
        words_list.sort()
        if words_list == word_list:
            lst.append(i)

    print(lst)


anagrams('laser', ['lazing', 'lazy',  'lacer'])
