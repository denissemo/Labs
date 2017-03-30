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
def bmx_precompile(p):
    d = {}
    len_p = len(p)
    for i in range(len(p)):
        d[ord(p[i])] = len_p - i
    return d


def bmx_search(s, p):
    d = bmx_precompile(p)
    # k - проход по text
    # j - проход по pattern
    # i - место начала прохода по text
    len_p = i = j = k = len(p)
    while j > 0 and i <= len(s):
        if s[k-1] == p[j-1]:
            k -= 1
            j -= 1
        else:
            i += d.get(ord(s[i]), len_p)
            j = len_p
            k = i
    if j <= 0:
        return k
    return None

returned = bmx_search(text, pattern)
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
