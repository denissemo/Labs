# Семенов Денис КНІТ 16-А
"""Условие: прямой поиск подстроки."""

from timeit import timeit
setup = '''
from string import ascii_letters
from random import choice, randint

def string_search(s, p):
    i = j = 0
    while j < len(p) and i <= len(s) - len(p):
        if s[i + j] == p[j]:
            j += 1
        else:
            i += 1
            j = 0
    return i if j == len(p) else None

letters = ascii_letters
text = ''.join(choice(letters) for i in range(108))
print('Source string:\\n', text)
pattern = ''
rand = randint(0, 104)
for c in range(4):
    pattern += text[rand]
    rand += 1
print('\\nRandomly selected substring == {} =='.format(pattern))
returned = string_search(text, pattern)
if returned is None:
    print('\\nElement not found...')
else:
    print('\\nSubstring |{}| was found at {} position'.format(pattern, returned))
print('\\nThe amount of memory, consumed by the string search algorithm {} bytes'
      .format(returned.__sizeof__()))
'''
time = timeit(setup, number = 1)
print('\nTime of algorithm execution {:1.3f} second'.format(time))
