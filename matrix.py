from sympy import Matrix


# Функция применения метода Крамера для решения системы линейных уравнений
def cramer_rule(A, B):
    # Вычисление определителя главной матрицы
    det_A = A.det()
    # Проверка на случай, если определитель главной матрицы равен нулю
    if det_A == 0:
        raise ValueError("Определитель матрицы коэффициентов равен нулю, метод Крамера не применим.")

    solutions = []
    print(A.shape) 
    print(B.shape)
    print(A.inverse_CH())
    # Проходим по каждому столбцу матрицы и вычисляем определитель со заменой столбца на вектор значений
    for i in range(A.shape[0]):
        Ai = A.copy()
        Ai[:, i] = B
        solutions.append(Ai.det() / det_A)

    return solutions


# Матрица коэффициентов системы уравнений
A = Matrix([
    [3, 2, -1],
    [1, -1, 1],
    [2, -3, -5]   
])
# Вектор значений
B = Matrix([8, -2, 1])

try:
    # Вызов функции для решения системы уравнений методом Крамера
    solutions = cramer_rule(A, B)
    # Вывод результатов
    print("Решение методом Крамера:")
    for i, sol in enumerate(solutions, start=1):
        print(f"x{i}: {sol}")
except ValueError as e:
    print(e)





# from sympy import Matrix
# import copy


# # Функция преобразрвание матрицы А и вектор-столбца B в расширенную матрицу
# def matrix_augmentation(A, B):
#     A_copy = copy.deepcopy(A)
#     for i in range(len(A_copy)):
#         A_copy[i].append(B[i])
#     return A_copy
    
#  # Матрица коэффициентов системы уравнений
# A = [
#     [3, 2, -1],
#     [1, -1, 1],
#     [2, -3, -5]   
# ]
# # Вектор значений
# B = [8, -2, 1]  
    
# # Определение расширенной матрицы [A|B]
# augmented_matrix = Matrix(matrix_augmentation(A,B))

# # Выполнение приведения матрицы к ступенчатому виду
# row_reduced_matrix, jaba = augmented_matrix.rref()


# print("x =", row_reduced_matrix[0, 3])
# print("y =", row_reduced_matrix[1, 3])
# print("z =", row_reduced_matrix[2, 3])












# ОБРАТНАЯ МАТРИЦА
# A = Matrix([
#     [3, 2, -1],
#     [1, -1, 1],
#     [2, -3, -5]   
# ])
# # Вектор значений
# B = Matrix([8, -2, 1])

# det = A.det()
# print(det)

# if det == 0:
#     print('определитель равен нулю, метод обратной матрицы не подходит')
# else:
#     reversed_matrix = A.inverse_CH()
#     res = reversed_matrix * B
    
#     print("x =", res[0])
#     print("y =", res[1])
#     print("z =", res[2])
    