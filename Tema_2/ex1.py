def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1

    for i in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence

n = int(input("Introduceti valoarea lui n: "))
result = generate_fibonacci(n)
print(f"Primele {n} numere din sirul Fibonacci sunt:  {result}")
