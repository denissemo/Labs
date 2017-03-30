# Семенов Денис КНІТ 16-А
"""Условие: алгоритм Вагнера-Фишера"""

from timeit import timeit
setup = '''
import numpy as np
while True:
    text = input('Please enter string: ')
    pattern = input('\\nPlease enter pattern: ')
    if text.isdigit() and pattern.isdigit():
        print('please enter string in text\\n')
        continue
    break
m = len(text)
n = len(pattern)
d = np.zeros((n + 1, m + 1), dtype = int)
'''

stmt = '''
for i in range(m + 1):
    d[i][0] = i
for j in range(n + 1):
    d[0][j] = j
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if text[i - 1] == pattern[j - 1]:
            d[i][j] = d[i - 1][j - 1]
        else:
            d[i][j] = 1 + min(d[i - 1][j], d[i - 1][j - 1], d[i][j - 1])
print('\\nNeed a |{}| conversion of string = {} ='.format(d[m][n], text))
print('\\nThe amount of memory, consumed by the WF search algorithm {} bytes'
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
