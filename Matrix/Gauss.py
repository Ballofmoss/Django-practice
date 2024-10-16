from sympy import Matrix, pprint
import copy


# Функция преобразрвание матрицы А и вектор-столбца B в расширенную матрицу
def matrix_augmentation(A, B):
    A_copy = copy.deepcopy(A)
    for i in range(len(A_copy)):
        A_copy[i].append(B[i])
    return A_copy
    
A = [
    [3, 2, -1],
    [1, -1, 1],
    [2, -3, -5]   
]
B = [8, -2, 1]  
    
# Определение расширенной матрицы [A|B]
augmented_matrix = Matrix(matrix_augmentation(A,B))

# Выполнение приведения матрицы к ступенчатому виду
row_reduced_matrix, rows_indexes = augmented_matrix.rref()

print("x =", row_reduced_matrix[0, 3])
print("y =", row_reduced_matrix[1, 3])
print("z =", row_reduced_matrix[2, 3])