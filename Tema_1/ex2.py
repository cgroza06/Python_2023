def number_of_vowels(input_string):
    count_vowels = 0
    vowels = set("aeiouAEIOU")

    for character in input_string:
        if character in vowels:
            count_vowels += 1

    return count_vowels

input_string = input("Introduceți un șir de caractere: ")
result = number_of_vowels(input_string)

print(f'Numărul de vocale din șir este: {result}')
