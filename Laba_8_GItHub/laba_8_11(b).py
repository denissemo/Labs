# Семенов Денис КНІТ 16-А
"""Условие: элементы линейного массива циклически сдвиньте на к позиций влево
(без выполнения лишних сдвигов)"""

import numpy as np


def shift_a(a, k):
    while k != 0:
        m = a[0]
        for i in range(len(a) - 1):
            a[i] = a[i + 1]
        a[len(a) - 1] = m
        k -= 1
    return a


flag = True
while True:
    try:
        len_a = int(input('Enter array length: '))
    except ValueError:
        print('You must enter integer number:)\n')
        continue
    if len_a >= 2:
        array = np.zeros(len_a)
        print(array)
        for i in range(len_a):
            try:
                array[i] = float(input(f'Input element of array {i + 1:d}: '))
            except ValueError:
                print('Please enter the number, you enter words!\n')
                flag = False
                break
        while flag:
            try:
                shift = int(
                    input('\nHow many positions need to move the array? '))
                if shift >= 0:
                    if shift > len_a:
                        shift %= len_a
                    print('\nShifted array\n', shift_a(array, shift))
                else:
                    print('Shift can not be negative!\n')
            except ValueError:
                print('You must enter integer number:)\n')
                continue
            else:
                break
    else:
        print('Array must be bigger...\n')
        continue
    ask = input('\nDo you want continue? [y/n]: ')
    if ask == 'y':
        flag = True
        continue
    else:
        break
