# Семенов Денис КНІТ 16-А
"""Условие: прямой поиск подстроки."""

from timeit import timeit
setup = '''
from string import ascii_letters
from random import choice, randint

letters = ascii_letters
while True:
    try:
        l_arr = int(input('Please enter length of string: '))
        if l_arr < 9:
            print('Please enter correctly number\\n')
            continue
        break
    except ValueError:
        print('Please enter int number\\n')
        continue
text = ''.join(choice(letters) for i in range(l_arr))
print('Source string:\\n', text)
pattern = ''
rand = randint(0, l_arr + 1)
for c in range(4):
    pattern += text[rand]
    rand += 1
'''

stmt = '''
def string_search(s, p):
    i = j = 0
    while j < len(p) and i <= len(s) - len(p):
        if s[i + j] == p[j]:
            j += 1
        else:
            i += 1
            j = 0
    return i if j == len(p) else None
    
print('\\nRandomly selected substring == {} =='.format(pattern))
returned = string_search(text, pattern)
if returned is None:
    print('\\nElement not found...')
else:
    print('\\nSubstring |{}| was found at {} position'.format(pattern, returned))
print('\\nThe amount of memory, consumed by the string search algorithm {} bytes'
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
