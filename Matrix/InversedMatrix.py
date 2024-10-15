from sympy import Matrix
# ОБРАТНАЯ МАТРИЦА
A = Matrix([
    [2, 3, -1],
    [3, -1, 4],  
    [5, -2, 2]   
])
# Вектор значений
B = Matrix([5, 13, 7])

det = A.det()
print(det)

if det == 0:
    print('определитель равен нулю, метод обратной матрицы не подходит')
else:
    inversed_matrix = A.inv()
    res = inversed_matrix * B
    
    print("x =", res[0])
    print("y =", res[1])
    print("z =", res[2])