# Семенов Денис КНІТ 16-А
"""Условие: бинарный поиск"""

from timeit import timeit
setup = '''
import numpy as np
from random import randint

def binary_search(a, x):
    s = 0
    e = len(a) - 1
    answer = None
    while s <= e:
        mid = (s + e) // 2
        if a[mid] == x:
            answer = mid
            break
        elif a[mid] > x:
            e = mid - 1
        elif a[mid] < x:
            s = mid + 1
    return answer

array = np.zeros(108, dtype = int)
for i in range(len(array)):
    array[i] = randint(0, 200)

print('Source array:\\n', array)
s_array = np.sort(array)
print('\\nSorted array:\\n', s_array)
c_elem = randint(0, 200)
print('\\nRandomly selected item from sequence:\\n == {} =='.format(c_elem))
returned = binary_search(s_array, c_elem)
if returned is None:
    print('\\nElement not found...')
else:
    print('\\nElement |{}| was found at {} position'.format(c_elem, returned))
print('\\nThe amount of memory, consumed by the binary search algorithm {} bytes'
      .format(returned.__sizeof__()))
'''
time = timeit(setup, number = 1)
print('\nTime of algorithm execution {:1.3f} second'.format(time))
