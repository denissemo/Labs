# Семенов Денис КНІТ 16-А
"""Условие: написать программу вычисления суммы тех элементов матрицы а,
номера строк и столюцов которых принадележит соответсвенно непустым множествам
s_1 и s_2"""

while True:
    n = 10
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    s_1 = {i for i in range(n)}
    s_2 = {i for i in range(n)}
    sums = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i in s_1 and j in s_2:
                sums += a[i][j]
    print('Сумма: ', sums)
    ask = input('\nПродолжаем? [y/n]: ')
    if ask == 'y':
        continue
    else:
        break
