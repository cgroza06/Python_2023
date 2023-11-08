def count_letter(string):
    string.lower()
    common_ch = ""
    common_ch_apparition = 0

    for i in "qwertyuiopasdfghjklxcvbnm":
        count = string.count(i)
        if count > common_ch_apparition:
            common_ch_apparition = count
            common_ch = i
    return common_ch

string = input("Introduceți un șir de caractere: ")

result = count_letter(string)
print(f"Cea mai frecventă literă în textul dat este {result}")