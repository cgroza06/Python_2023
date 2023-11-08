def set_operations(a, b):
    intersection = list(set(a) & set(b))

    union = list(set(a) | set(b))

    a_minus_b = list(set(a) - set(b))

    b_minus_a = list(set(b) - set(a))

    return intersection, union, a_minus_b, b_minus_a

list_a = []
n = int(input("Introduceti numarul de elemente din lista A: "))
for i in range(n):
    num_a = int(input(f"Introduceti elementul {i + 1}: "))
    list_a.append(num_a)

list_b = []
m = int(input("Introduceti numarul de elemente din lista B: "))
for j in range(m):
    num_b = int(input(f"Introduceti elementul {j + 1}: "))
    list_b.append(num_b)

intersection, union, a_minus_b, b_minus_a = set_operations(list_a, list_b)

print("Intersectia dintre a si b:", intersection)
print("Reuniunea dintre a si b:", union)
print("Elemente in a dar nu în b:", a_minus_b)
print("Elemente in b dar nu în a:", b_minus_a)
