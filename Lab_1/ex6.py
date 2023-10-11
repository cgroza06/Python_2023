def is_palindrome(number):
    number_str = str(number)
    reverse_number = number_str[::-1]

    if number_str == reverse_number:
        return True
    else:
        return False

number = int(input("Introduceți un număr: "))
result = is_palindrome(number)

if result:
    print(f"{number} este un număr palindrom.")
else:
    print(f"{number} nu este un număr palindrom.")
