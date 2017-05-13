# Семенов Денис КНІТ 16-А
"""Условие: Сформировать процедуру подсчета количества различных представлений
заданного натурального числа n в виде суммы не менее двух попарно различных
натуральных слагаемых. Представления, отличающиеся лишь порядком слагаемых,
различными не считаются."""

import numpy as np

def number_decompose_rec(n, i):
    """ Высчитывает кол-во представлений.
    
    :param n: заданное натуральное число
    :param i: кол-во слагаемых
    :return: кол-во представлений
    """
    if n == 0 and i == 0:
        return 1
    if n <= 0 or i <= 0:
        return 0
    return number_decompose_rec(n - i, i) + number_decompose_rec(n - 1, i - 1)

def number_decompose_rec_stack(n):
    """ Функция подсчета количества различных представлений заданого числа.
     Рекурсивно

    :param n: заданное натуральное число
    :return: количество различных представлений числа n
    """
    s = []
    if n == 0 or n == 1:
        return 0
    for i in range(1, n):
        s.append(number_decompose_rec(n, i))
    return max(s)


def number_decompose_iter(n):
    """ Функция подсчета количества различных представлений заданого числа.
     Итерационно

    :param n: заданное натуральное число 
    :return: количество различных представлений числа n 
    """
    a = 0
    n1 = n
    c = 0  # количество представлений числа n
    while n1 >= 0:
        a += 1
        n1 -= a
    mas = np.zeros(a - 1, dtype = int)
    for i in range(0, a - 1):
        mas[i] = i + 1
    if n1 != 0:
        mas[a - 2] = mas[a - 3] + a + 1 + n1
    a -= 1
    for i in range(0, a):
        pass
    c += 1
    while a > 1:
        for j in range(a - 2, -1, -1):
            temp1 = mas[j]
            temp2 = mas[a - 1]
            while mas[j] + 1 < mas[a - 1] - 1:
                mas[j] += 1
                mas[a - 1] -= 1
                n1 = 0
                for i in range(0, a - 1):
                    for i1 in range(i + 1, a):
                        if mas[i] == mas[i1]:
                            n1 = 1
                if n1 == 0:
                    for i in range(0, a):
                        pass
                    c += 1
            mas[j] = temp1
            mas[a - 1] = temp2
        mas[a - 2] += mas[a - 1]
        a -= 1
    if n > 5:
        return c + 1
    else:
        return c


while True:
    while True:
        try:
            num = int(input('Please enter number → '))
            if num < 3:
                print('Please enter bigger number\n')
                continue
            break
        except ValueError:
            print('Number must be integer!\n')
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
        print('\nRecursion version ↓\nThe number of different representations '
              'of {} number → {}'.format(num, number_decompose_rec_stack(num)))
    else:
        print('\nIteration version ↓\nThe number of different representations '
              'of {} number → {}'.format(num, number_decompose_iter(num)))
    ask = input('\nDo you want to try again? [1/0]: ')
    if ask == '1':
        print()
        continue
    else:
        break
