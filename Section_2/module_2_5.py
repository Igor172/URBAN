def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix1 = []
        matrix.append(matrix1)
        for j in range(m):
            matrix1.append(value)
    return matrix


result = get_matrix(3, 4, 5)
print(result)