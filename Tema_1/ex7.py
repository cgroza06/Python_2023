def extract_number(string):
    n = ""
    i = 0
    no_found = False

    while i < len(string) and no_found == False:
        if "0" <= string[i] <= "9":
            while i < len(string) and ("0" <= string[i] <= "9"):
                n += string[i]
                i += 1
            no_found = True
        else:
            i += 1
    if n != "":
        return int(n)
    else:
        return None


x = input("Introduceți un text: ")
result = extract_number(x)

if result is not None:
    print(f"Numărul extras din text este: {result}")
else:
    print("Nu s-a găsit niciun număr în text.")
