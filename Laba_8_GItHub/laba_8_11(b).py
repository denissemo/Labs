# Семенов Денис КНІТ 16-А
"""Условие: элементы линейного массива циклически сдвиньте на к позиций влево
(без выполнения лишних сдвигов)"""

import numpy as np
flag = True
while True:
    try:
        len_a = int(input('Enter array length: '))
    except ValueError:
        print('You must enter integer number:)\n')
        continue
    if len_a >= 2:
        array = np.zeros(len_a)
        for i in range(len_a):
            try:
                array[i] = float(input(f'Input element of array {i + 1:d}: '))
            except ValueError:
                print('Please enter the number, you enter words!\n')
                flag = False
                break
        while flag:
            try:
                shift = int(input('\nHow many positions need to move the array? '))
                if shift >= 0:
                    m_array = np.roll(array, -shift)
                    print('\nShifted array\n', m_array)
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
