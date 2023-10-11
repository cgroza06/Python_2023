def convert_to_lower_with_underscores(upper_camel_case):
    result = upper_camel_case[0].lower()

    for char in upper_camel_case[1:]:
        if char.isupper():
            result += '_' + char.lower()
        else:
            result += char
    return result

upper_camel_case = input("Introduceți un șir UpperCamelCase: ")

result = convert_to_lower_with_underscores(upper_camel_case)

print(f'Șirul convertit este: {result}')
