# Семенов Денис КНІТ 16-А
"""Условие: поверните квадратный массив на 90 грудусов по часовой стрелке."""

import numpy as np
while True:
    try:
        while True:
            n = int(input('Input tapes: '))
            if n < 2:
                print('input correct number\n')
                continue
            break
        while True:
            m = int(input('Input columns: '))
            if m < 2:
                print('input correct number\n')
                continue
            break
    except ValueError:
        print('Please input integer number\n')
        continue
    if n == m:
        array = np.zeros((n, m))
        print(array)
        flag = False
        for i in range(n):
            for j in range(m):
                try:
                    array[i][j] = float(input('Input element of array %d%d: ' %
                                              (i + 1, j + 1)))
                except ValueError:
                    print('Please enter the number, you enter words!\n')
                    flag = True
                    break
            if flag:
                break
        if not flag:
            print('\nSource array:\n', array)
            s = ''
            for i in range(0, len(array)):
                for j in range(-1, -len(array) - 1, -1):
                    s += str(array[j][i]) + ' '
                s += '\n'
            print('\nArray turn to 90 degrees:\n{}'.format(s) )
    else:
        print('Array must be a square!\n')
        continue
    ask = input('\nDo you want continue? [y/n]: ')
    if ask == 'y':
        print()
        continue
    else:
        break
