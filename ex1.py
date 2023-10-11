def gcd(x, y):
    if x==0:
        return y
    else:
        return gcd (y%x,x)

def gcd_multiple_no(*list_of_numbers):
    res = 0
    for number in list_of_numbers:
        if res==0:
            res=number
        else:
            res=gcd(res,number)
            if res==1:
                return 1
    return res

console_numbers = list()
n=int(input("Introduceți numărul de numere: "))
for i in range(n):
    a=int(input("Introduceți numărul:  "))
    console_numbers.append(a)

result = gcd_multiple_no(*console_numbers)
print(f"Cel mai mare divizor comun al numerelor este: {result}")