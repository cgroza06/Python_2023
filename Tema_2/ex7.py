def palindrome_tuple(list):
    no_of_palindromes = 0
    max_palindrome = -1
    for i in list:
        if str(i) == str(i)[::-1]:
            no_of_palindromes += 1
            if i > max_palindrome:
                max_palindrome = i
    x = (no_of_palindromes,max_palindrome)
    return x

string_list = input("Introduceti elementele listei, separate de un spatiu: ")
string_list = string_list.split()
list = []
for i in string_list:
    list.append(int(i))

result = palindrome_tuple(list)
print(result)
