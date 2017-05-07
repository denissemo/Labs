# Семенов Денис КНІТ 16-А
"""Условие: найти НОД рекурсивно и итерационно"""

def rec_nod(n, m):
    """ НОД двух чисел, рекурсивно.
    
    :param n: первое число выражения
    :param m: второе число выражения
    :return: НОД чисел n и m
    """
    if m == 0:
        return n
    else:
        return rec_nod(m, n % m)

def iter_nod(n, m):
    """ НОД двух чисел, итерационно.
    
    :param n: первое число выражения
    :param m: второе число выражения
    :return: НОД чисел n и m
    """
    while m:
        n, m = m, n % m
    return n


while True:
    while True:
        try:
            num1 = int(input('Please enter first number → '))
            if num1 < 0:
                print('Number must be positive!')
                continue
            break
        except ValueError:
            print('Number must be integer!')
            continue
    while True:
        try:
            num2 = int(input('Please enter second number → '))
            if num2 < 0:
                print('Number must be positive!')
                continue
            break
        except ValueError:
            print('Number must be integer!')
            continue
    while True:
        try:
            rec_or_iter = int(input('\nHow do you want to use the function?'
                                    '\n 1 - Recursively\n 2 - Iteratively\n→ '))
            if rec_or_iter not in range(1, 3):
                print('input correct number\n')
                continue
            break
        except ValueError:
            print('Please enter integer number!\n')
            continue
    if rec_or_iter == 1:
        print('\nRecursive version ↓\n NOD of {} and {} → {}'
            .format(num1, num2, rec_nod(num1, num2)))
    else:
        print('\nIteration version ↓\n NOD of {} and {} → {}'
            .format(num1, num2, iter_nod(num1, num2)))
    ask = input('\nDo you want to try again? [1/0]: ')
    if ask == '1':
        print()
        continue
    else:
        break
