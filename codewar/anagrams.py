# Write a function that will find all the anagrams of a word from a list.
# You will be given two inputs a word and an array with words.
# You should return an array of all the anagrams or an empty array if there are none.

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
