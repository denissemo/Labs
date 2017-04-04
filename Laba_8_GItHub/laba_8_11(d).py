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
            l = 0
            mult_diag = 1
            while l != n - 1:
                subtr = array[l, l]
                mult_diag *= subtr
                for i in range(l + 1, n):
                    minus = array[i][l] / subtr
                    for j in range(n):
                        array[i, j] -= minus * array[l][j]
                l += 1
            print('\nDeterminant of array:\n', mult_diag * array[l][l])
    else:
        print('Array must be a square!\n')
        continue
    ask = input('\nDo you want continue? [y/n]: ')
    if ask == 'y':
        print()
        continue
    else:
        break
