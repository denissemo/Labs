# Семенов Денис КНІТ 16-А
"""Условие: линейный поиск"""

from timeit import timeit
setup = '''
import numpy as np
from random import choice
from string import ascii_letters

letters = ascii_letters
while True:
    try:
        l_arr = int(input('Please enter length of array: '))
        if l_arr < 1:
            print('Please enter correctly number\\n')
            continue
        break
    except ValueError:
        print('Please enter int number\\n')
        continue
array = np.zeros(l_arr, dtype = str)
for j in range(len(array)):
    array[j] = choice(letters)
'''

stmt = '''
def linear_search(a, x):
    a = np.append(a, [x])
    i = 0
    while a[i] != x:
        i += 1
    return i if i < len(a) - 1 else None
    
print('Source array:\\n', array)
c_elem = choice(letters)
print('\\nRandomly selected item from sequence:\\n == {} =='.format(c_elem))
returned = linear_search(array, c_elem)
if returned is None:
    print('\\nElement not found...')
else:
    print('\\nElement |{}| was found at {} position'.format(c_elem, returned))
print('\\nThe amount of memory, consumed by the linear search algorithm {} bytes'
      .format(array.__sizeof__()))
'''
while True:
    time = timeit(stmt, setup, number = 1)
    print('\nTime of algorithm execution {:f} second'.format(time))
    ask = input('\nDo you want continue?: ').lower()
    if ask == 'y':
        continue
    else:
        break
