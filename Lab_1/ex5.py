def spiral_order(matrix):
    if not matrix:
        return ""

    result = []
    while matrix:
        # dreapta
        result.extend(matrix[0])
        matrix.pop(0)

        # jos
        for row in matrix:
            if row:
                result.append(row[-1])
                row.pop()

        # stanga
        if matrix:
            result.extend(matrix[-1][::-1])
            matrix.pop()

        # sus
        for row in reversed(matrix):
            if row:
                result.append(row[0])
                row.pop(0)

    return ''.join(result)

print("Introduceți matricea de caractere, fiecare rând pe o linie separată:")
matrix = []
while True:
    row = input()
    if not row:
        break
    matrix.append(list(row))

result = spiral_order(matrix)

print(result)
