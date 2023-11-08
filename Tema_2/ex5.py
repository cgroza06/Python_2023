def replace_below_main_diagonal_with_zeros(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    for i in range(num_rows):
        for j in range(num_columns):
            if i > j:
                matrix[i][j] = 0

    return matrix

print("Introduceți matricea de caractere, fiecare rand pe o linie separata:")
matrix = []
while True:
    row = input()
    row = row.split()
    if not row:
        break
    matrix.append(list(row))

result = replace_below_main_diagonal_with_zeros(matrix)
for row in result:
    print(row)

