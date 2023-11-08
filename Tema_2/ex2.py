def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    x = 3
    while x * x <= n:
        if n % x == 0:
            return False
        x += 2
    return True

def prime_numbers_in_list(numbers):
    prime_list = []
    for num in numbers:
        if is_prime(num):
            prime_list.append(num)
    return prime_list

input_list = []
n = int(input("Introduceti numarul de elemente din lista: "))
for i in range(n):
    num = int(input(f"Introduceti elementul {i + 1}: "))
    input_list.append(num)

result = prime_numbers_in_list(input_list)
print("Numere prime din lista:", result)
