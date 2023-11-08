class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data= [[0 for j in range(cols)] for i in range(rows)]

    def get(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            return None

    def set(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.data[j][i] = self.data[i][j]
        return transposed

    def multiply(self, other):
        if self.cols != other.rows:
            return None  # Matrix multiplication not possible
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def apply(self, transformation):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = transformation(self.data[i][j])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])


matrix = Matrix(3, 3)

# Set values
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 5)
matrix.set(1, 2, 6)
matrix.set(2, 0, 7)
matrix.set(2, 1, 8)
matrix.set(2, 2, 9)

print(matrix)
transposed_matrix = matrix.transpose()
print(transposed_matrix)

matrix_a = Matrix(2, 3)
matrix_a.set(0, 0, 2)
matrix_a.set(0, 1, 3)
matrix_a.set(0, 2, 4)
matrix_a.set(1, 0, 5)
matrix_a.set(1, 1, 6)
matrix_a.set(1, 2, 7)

matrix_b = Matrix(3, 2)
matrix_b.set(0, 0, 1)
matrix_b.set(0, 1, 2)
matrix_b.set(1, 0, 3)
matrix_b.set(1, 1, 4)
matrix_b.set(2, 0, 5)
matrix_b.set(2, 1, 6)

result = matrix_a.multiply(matrix_b)
print(result)

matrix.apply(lambda x: x + 10)
print(matrix)

