def could_not_see(matrix):
    n = len(matrix)
    m = len(matrix[0])
    too_short = []
    for j in range(m):
        max_height = 0
        for i in range(n):
            if matrix[i][j] <= max_height:
                too_short.append((i,j))
            else:
                max_height = matrix[i][j]
    return too_short

print("Introduceți matricea de caractere, fiecare rand pe o linie separata:")
matrix = []
while True:
    row = input()
    row = row.split()
    if not row:
        break
    row = [int(num) for num in row]
    matrix.append(list(row))

print(could_not_see(matrix))
