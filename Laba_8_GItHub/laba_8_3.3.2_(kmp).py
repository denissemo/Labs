# Семенов Денис КНІТ 16-А
"""Условие: алгоритм Кнута-Морриса-Пратта"""

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
def prefix_func(p):
    d = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[j] != p[i]:
            j = d[j-1]
        if p[j] == p[i]:
            j += 1
        d[i] = j
    return d

def kmp_search(s, p):
    d = prefix_func(p)
    i = j = 0
    while i < len(s) and j < len(p):
        if p[j] == s[i]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = d[j-1]
    else:
        if j == len(p):
            return i - j
        return None

returned = kmp_search(text, pattern)
if returned is None:
    print('\\nElement not found...')
else:
    print('\\nPattern |{}| was found at {} position'.format(pattern, returned))
print('\\nThe amount of memory, consumed by the KMP search algorithm {} bytes'
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
