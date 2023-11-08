def group_by_rhyme(list_of_words):
    rhyme_dictionary = {}
    for i in list_of_words:
        if i[-2:] in rhyme_dictionary:
            rhyme_dictionary[i[-2:]].append(i)
        else:
            rhyme_dictionary[i[-2:]]=[i]
    return list(rhyme_dictionary.values())

list_of_words = input("Introduceti o lista de cuvinte, separate de un spatiu: ")
list_of_words = list_of_words.split()
print(group_by_rhyme(list_of_words))
