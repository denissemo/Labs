# Семенов Денис КНІТ 16-А
"""Условие: линейный поиск"""

import numpy as np
from random import choice, randint
from string import ascii_uppercase

def linear_search(a, x):
    a = np.append(a, [x])
    i = 0
    while a[i] != x:
        i += 1
    return i if i < len(a) - 1 else None

while True:
    letters = ascii_uppercase
    array = np.zeros(randint(10, 15), dtype = str)
    for j in range(len(array)):
        array[j] = choice(letters)

    print('Source array:\n', array)
    c_elem = choice(letters)
    print('\nRandomly selected item from sequence:\n == {} =='.format(c_elem))
    returned = linear_search(array, c_elem)
    if returned is None:
        print('\nElement not found...')
    else:
        print('\nElement {} was found at {} position'.format(c_elem, returned))

    ask = input('\nDo you want try again? [y/n]: ')
    if ask == 'y':
        continue
    else:
        break
