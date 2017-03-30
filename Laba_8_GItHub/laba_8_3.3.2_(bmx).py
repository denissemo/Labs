# Семенов Денис КНІТ 16-А
"""Условие: алгоритм Бойера-Мура-Хорспула"""

from timeit import timeit
setup = '''
from random import choice

while True:
    try:
        l_arr = int(input('Please enter length of string: '))
        if l_arr < 4:
            print('Please enter correctly number\\n')
            continue
        break
    except ValueError:
        print('Please enter int number\\n')
        continue
text = ''.join(choice('abc') for i in range(l_arr))
print('Source string:\\n', text)
pattern = ''.join(choice('abc') for j in range(4))
print('\\nRandomly selected pattern == {} =='.format(pattern))
'''

stmt = '''
def bmx_search(s, p, n, m):
    d = [m] * (ord(max(max(text), max(pattern))) + 1)
    for i in range(m - 1):
        d[ord(p[i])] = m - i - 1
        p_elem = -1
        i = 0
        while n - i >= m and p_elem == -1:
            j = m - 1
            while s[i + j] == p[j]:
                if j == 0:
                    p_elem = i
                    break
                j -= 1
            i += d[ord(s[i + m - 1])]
        if p_elem != -1:
            return p_elem
        else:
            return None

returned = bmx_search(text, pattern, len(text), len(pattern))
if returned is None:
    print('\\nElement not found...')
else:
    print('\\nPattern |{}| was found at {} position'.format(pattern, returned))
print('\\nThe amount of memory, consumed by the BMX search algorithm {} bytes'
      .format(text.__sizeof__()))
'''
while True:
    time = timeit(stmt, setup, number = 1)
    print('\nTime of algorithm execution {:f} second'.format(time))
    ask = input('\nDo you want continue?: ').lower()
    if ask == 'y':
        continue
    else:
        break
