def string_occurrences(string1,string2):
    return string1.count(string2)

first_string=input("Introduceți primul șir: ")
second_string=input("Introduceți al doilea șir: ")
result = string_occurrences(first_string,second_string)

print(f'Numărul de apariții ale "{second_string}" în "{first_string}" este: {result}')