def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix
result_1 = get_matrix(2, 2, 15)
result_2 = get_matrix(3, 4, 25)
result_3 = get_matrix(3, 2, 10)
print(f'Матрица 2х2 со значениями 15: {result_1}')
print(f'Матрица 3х4 со значениями 25: {result_2}')
print(f'Матрица 3х2 со значениями 10: {result_3}')