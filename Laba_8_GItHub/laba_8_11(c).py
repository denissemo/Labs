# Семенов Денис КНІТ 16-А
"""Условие: выполните произведение двух квадратных матриц (массивов), учтите
размерность"""

import numpy as np

def fill(x):
    """Заполняет массив данными"""
    flag = False
    for i in range(n):
        for j in range(m):
            try:
                x[i][j] = float(input(
                            f'Input element of array {i + 1:d}{j + 1:d}: '))
            except ValueError:
                print('Please enter the number, you enter words!\n')
                flag = True
                break
        if flag:
            return flag

def tapes():
    """Ввод элементов строки"""
    while True:
        x = int(input('Input tapes: '))
        if x < 2:
            print('input correct number\n')
            continue
        return x

def columns():
    """Ввод элементов колонки"""
    while True:
        x = int(input('Input columns: '))
        if x < 2:
            print('input correct number\n')
            continue
        return x

while True:
    try:
        print('First array:\n')
        n_1 = tapes()
        m_1 = columns()
    except ValueError:
        print('Please input integer number\n')
        continue
    try:
        print('\nSecond array:\n')
        n_2 = tapes()
        m_2 = columns()
    except ValueError:
        print('Please input integer number\n')
        continue
    if n_1 == n_2 and m_1 == m_2 and n_1 == m_1:
        n = n_1 = n_2
        m = m_1 = m_2
        array_1 = np.zeros((n, m))
        array_2 = np.zeros((n, m))
        array_3 = np.zeros((n, m))
        print('\nNow you fill the array 1:\n')
        fill_a_1 = fill(array_1)
        print('\nNow you fill the array 2:\n')
        fill_a_2 = fill(array_2)
        if not (fill_a_1 or fill_a_2):
            print('\nSource array 1:\n', array_1)
            print('\nSource array 2:\n', array_2)
            for i in range(n):
                for j in range(n):
                    for c in range(n):
                        array_3[i][j] += array_1[i][c] * array_2[c][j]
            print('\nMultiplication of arrays:\n', array_3)
        else:
            print('An error occurred, try again...\n')
            continue
    else:
        print('Arrays must be a square and equal!\n')
        continue
    ask = input('\nDo you want continue? [y/n]: ')
    if ask == 'y':
        print()
        continue
    else:
        break
