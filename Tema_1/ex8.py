def binary_number(x):
    binary = bin(x)
    no_of_one = binary.count("1")
    return no_of_one

n = int(input("Introduceti un numar: "))
result = binary_number(n)

print(f"Numărul de biți cu valoarea 1 în reprezentarea binară a numărului {n} este: {result}")