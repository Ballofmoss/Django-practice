from sympy import Matrix


# Функция применения метода Крамера для решения системы линейных уравнений
def cramer_rule(A, B):
    # Вычисление определителя главной матрицы
    det_A = A.det()
    # Проверка на случай, если определитель главной матрицы равен нулю
    if det_A == 0:
        raise ValueError("Определитель матрицы коэффициентов равен нулю, метод Крамера не применим.")

    solutions = []
    # print(A.shape) 
    # print(B.shape)
    # print(A.inverse_CH())
    # Проходим по каждому столбцу матрицы и вычисляем определитель со заменой столбца на вектор значений
    for i in range(A.shape[0]):
        Ai = A.copy()
        Ai[:, i] = B
        solutions.append(Ai.det() / det_A)

    return solutions


# Матрица коэффициентов системы уравнений
A = Matrix([
    [1, 2, 1],
    [3, -5, 3],  
    [2, -7, -1]   
])
# Вектор значений
B = Matrix([4, 1, 8])

try:
    # Вызов функции для решения системы уравнений методом Крамера
    solutions = cramer_rule(A, B)
    # Вывод результатов
    print("Решение методом Крамера:")
    for i, sol in enumerate(solutions, start=1):
        print(f"x{i}: {sol}")
except ValueError as e:
    print(e)
