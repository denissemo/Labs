# Семенов Денис КНІТ 16-А
"""Условие: бинарный поиск"""

from timeit import timeit
setup = '''
import numpy as np
from random import randint

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
array = np.zeros(l_arr, dtype = int)
for i in range(len(array)):
    array[i] = randint(0, 200)
'''

stmt = '''   
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
      .format(s_array.__sizeof__()))
'''
while True:
    time = timeit(stmt, setup, number = 1)
    print('\nTime of algorithm execution {:f} second'.format(time))
    ask = input('\nDo you want continue?: ').lower()
    if ask == 'y':
        continue
    else:
        break
