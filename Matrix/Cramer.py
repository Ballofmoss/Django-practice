from sympy import Matrix



def cramer_rule(A, B):

    det_A = A.det()
   
    if det_A == 0:
        raise ValueError("Определитель матрицы равен нулю, метод Крамера не подходит")

    solutions = []

    # Проходим по каждому столбцу матрицы и вычисляем определитель со заменой столбца на вектор значений
    for i in range(A.shape[0]):
        Ai = A.copy()
        Ai[:, i] = B                
        solutions.append(Ai.det() / det_A)

    return solutions


A = Matrix([
    [1, 2, 1],
    [3, -5, 3],  
    [2, -7, -1]   
])
B = Matrix([4, 1, 8])

try:
    solutions = cramer_rule(A, B)
    print("Решение методом Крамера:")
    for i, sol in enumerate(solutions, start=1):
        print(f"x{i}: {sol}")
except ValueError as e:
    print(e)
