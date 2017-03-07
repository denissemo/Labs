# Семенов Денис КНІТ 16-А
"""Условие: вычислите определитель квадратной матрицы (массива)."""

import numpy as np
while True:
    try:
        while True:
            n = int(input('Input tapes: '))
            if n < 1:
                print('input correct number\n')
                continue
            break
        while True:
            m = int(input('Input columns: '))
            if m < 1:
                print('input correct number\n')
                continue
            break
    except ValueError:
        print('Please input integer number\n')
        continue
    if n == m:
        array = np.zeros((n, m))
        flag = False
        for i in range(n):
            for j in range(m):
                try:
                    array[i][j] = float(input(
                        f'Input element of array {i + 1:d}{j + 1:d}: '))
                except ValueError:
                    print('Please enter the number, you enter words!\n')
                    flag = True
                    break
            if flag:
                break
        if not flag:
            print('\nSource array:\n', array)
            array = np.linalg.det(array)
            print('\nDeterminant of array:\n', array)
    else:
        print('Array must be a square!\n')
        continue
    ask = input('\nDo you want continue? [y/n]: ')
    if ask == 'y':
        print()
        continue
    else:
        break
