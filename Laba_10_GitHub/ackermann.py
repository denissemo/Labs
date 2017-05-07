# Семенов Денис КНІТ 16-А
"""Условие: Вычислить функцию Аккермана рекурсивно и итерационно"""

def rec_ackermann(n, m):
    """ Рекурсивная функция Аккермана.
    
    :param n: первое неотрицательное целое число
    :param m: второе неотрицательное целое число
    :return: значение функции Аккермана
    """
    if n == 0:
        return m + 1
    elif n > 0 and m == 0:
        return rec_ackermann(n - 1, 1)
    else:
        return rec_ackermann(n - 1, rec_ackermann(n, m - 1))


def iter_ackermann(n, m):
    """ Нерекурсивная функция Аккермана.

    :param n: первое неотрицательное целое число
    :param m: второе неотрицательное целое число
    :return: значение функции Аккермана
    """
    stack = [n]
    while stack:
        n = stack.pop()
        if n == 0 or m == 0:
            m += n + 1
        else:
            n -= 1
            stack.append(n)
            n += 1
            stack.append(n)
            m -= 1
    return m


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
        print('\nRecursive version of Ackermann function ↓\n Number {} and {} → {}'
            .format(num1, num2, rec_ackermann(num1, num2)))
    else:
        print('\nIteration version of Ackermann function ↓\n Number {} and {} → {}'
            .format(num1, num2, iter_ackermann(num1, num2)))
    ask = input('\nDo you want to try again? [1/0]: ')
    if ask == '1':
        print()
        continue
    else:
        break
