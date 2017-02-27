# Семенов Денис КНІТ 16-А
"""Условие: дано натуральное число n, вывести на экран все натуральные числа,
меньше n и взаимно простые с ним"""

def gcd(a, b):
    """Euclid's algorithm"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

while True:
    try:
        n = int(input('Enter natural number: '))
    except ValueError:
        print('please enter number!\n')
        continue
    if n < 1:
        print('number not natural, try again!\n')
        continue
    elif n == 1:
        print('Relatively prime numbers:', n)
        ask = input('\nDo you want continue? [y/n]: ')
        if ask == 'y':
            continue
        else:
            break
    s_n = {i + 1 for i in range(n - 1)}
    print('Relatively prime numbers:')
    print(set(j for j in s_n if gcd(j, n) == 1))
    print('\n')
    ask = input('Do you want continue? [y/n]: ')
    if ask == 'y':
        continue
    else:
        break
