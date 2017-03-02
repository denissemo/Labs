# Семенов Денис КНІТ 16-А
"""Условие: поверните квадратный массив на 90 грудусов по часовой стрелке"""

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
        i_1 = 0
        flag = False
        for i in range(n-1, -1, -1):
            i_1 += 1
            for j in range(m):
                try:
                    array[i][j] = float(input('Input element of matrix %d%d: ' %
                                    (i_1, j + 1)))
                except ValueError:
                    print('Please enter the number, you enter words!\n')
                    flag = True
                    break
            if flag:
                break
        if not flag:
            array = np.swapaxes(array, 0, 1)
            print('Array turn to 90 degrees:\n', array)
    else:
        print('Array must be a square!\n')
        continue
    ask = input('Do you want continue? [y/n]: ')
    if ask == 'y':
        print()
        continue
    else:
        break
