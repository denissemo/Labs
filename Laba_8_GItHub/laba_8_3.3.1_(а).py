# Семенов Денис КНІТ 16-А
"""Условие: линейный поиск"""

from timeit import timeit
setup = '''
import numpy as np
from random import choice
from string import ascii_letters

def linear_search(a, x):
    a = np.append(a, [x])
    i = 0
    while a[i] != x:
        i += 1
    return i if i < len(a) - 1 else None


letters = ascii_letters
array = np.zeros(108, dtype = str)
for j in range(len(array)):
    array[j] = choice(letters)

print('Source array:\\n', array)
c_elem = choice(letters)
print('\\nRandomly selected item from sequence:\\n == {} =='.format(c_elem))
returned = linear_search(array, c_elem)
if returned is None:
    print('\\nElement not found...')
else:
    print('\\nElement |{}| was found at {} position'.format(c_elem, returned))
print('\\nThe amount of memory, consumed by the linear search algorithm {} bytes'
      .format(returned.__sizeof__()))
'''
time = timeit(setup, number = 1)
print('\nTime of algorithm execution {:1.3f} second'.format(time))
