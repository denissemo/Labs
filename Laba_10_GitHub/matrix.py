# Семенов Денис КНІТ 16-А
""" Условие:
Найти: сумму элементов квадратной матрицы;
       произведение элементов квадратной матрицы.
Выполнить: поиск элемента с заданым значением в квадратной матрице."""

import numpy as np

def matrix_sum_rec_index(a, n, m):
    """ Вычисляет сумму элементов квадратной матрицы рекурсивно.
    
    :param a: исходный массив
    :param n: длина исходной матрицы
    :param m: длина исходной матрицы
    :returns: индексы элементов матрицы
    """
    if n == 1:
        return matrix_sum_rec_add(a, m, 0)
    else:
        return matrix_sum_rec_index(a, n - 1, m) + matrix_sum_rec_add(a, m, n - 1)

def matrix_sum_rec_add(a, n, m):
    """ Вычисляет сумму элементов квадратной матрицы рекурсивно.

    :param a: исходный массив
    :param n: длина исходной матрицы        
    :param m: длина исходной матрицы
    :return: сумму элементов матрицы
    """
    if n == 1:
        return a[m][0]
    else:
        return matrix_sum_rec_add(a, n - 1, m) + a[m][n - 1]


def matrix_sum_iter(a):
    """ Вычисляет сумму элементов квадратной матрицы итеративно.
     
    :param a: исходная матрица
    :return: сумму элементов матрицы
    """
    sum_mat = 0
    for i in range(len(a)):
        for j in range(len(a)):
            sum_mat += a[i][j]
    return sum_mat


def matrix_mult_rec_index(a, n, m):
    """ Вычисляет произведение элементов квадратной матрицы рекурсивно.

    :param a: исходный массив
    :param n: длина исходной матрицы
    :param m: длина исходной матрицы
    :returns: индексы элементов матрицы
    """
    if n == 1:
        return matrix_mult_rec_add(a, m, 0)
    else:
        return matrix_mult_rec_index(a, n - 1, m) * matrix_mult_rec_add(a, m,
                                                                      n - 1)

def matrix_mult_rec_add(a, n, m):
    """ Вычисляет произведение элементов квадратной матрицы рекурсивно.

    :param a: исходный массив
    :param n: длина исходной матрицы        
    :param m: длина исходной матрицы
    :return: произведение элементов матрицы
    """
    if n == 1:
        return a[m][0]
    else:
        return matrix_mult_rec_add(a, n - 1, m) * a[m][n - 1]


def matrix_mult_iter(a):
    """ Вычисляет произведение элементов квадратной матрицы итеративно.

    :param a: исходная матрица
    :return: произведение элементов матрицы
    """
    mult_mat = 1
    for i in range(len(a)):
        for j in range(len(a)):
            mult_mat *= a[i][j]
    return mult_mat

c1 = 0
c2 = 0
def matrix_search_elem_rec(row, col, c, a):
    """ Поиск заданого элемента рекурсивно.
    
    :param row: индекс строки
    :param col: индекс колонки
    :param c: искомый элемент
    :param a: исходная матрица
    :return: положение искомого элемента
    """
    if a[row][col] == c:
        global c1, c2
        c1, c2 = row, col
    else:
        if col + 1 < len(a[0]):
            matrix_search_elem_rec(row, col + 1, c, a)
        elif row + 1 < len(a[1]):
            matrix_search_elem_rec(row + 1, 0, c, a)


def matrix_search_elem_iter(a, c):
    """ Поиск заданого элемента итерационно.
    
    :param a: исходная матрица
    :param c: искомый элемент
    :return: положение искомого элемента
    """
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == c:
                return i, j
    else:
        return None


while True:
    while True:
        try:
            matrix_size = int(input('Please enter size of matrix like [3x3].\nYou '
            'can enter only one number, because matrix are square:)\n→ '))
            if matrix_size < 2:
                print('input correct number\n')
                continue
            break
        except ValueError:
            print('Please enter integer number!\n')
            continue
    while True:
        try:
            matrix_fill = int(input('\nHow you want to fill matrix?\n 1 - Manually\n '
                                    '2 - Randomly\n→ '))
            matrix = np.zeros((matrix_size, matrix_size), dtype = int)
            if matrix_fill == 1:
                flag = False
                for i in range(matrix_size):
                    for j in range(matrix_size):
                        try:
                            matrix[i][j] = float(
                                input('Input element of matrix {}{} → '
                                      .format(i + 1, j + 1)))
                        except ValueError:
                            print('Please enter the number, you enter words!')
                            flag = True
                            break
                    if flag:
                        break
                if not flag:
                    break
            elif matrix_fill == 2:
                matrix = np.random.randint(1, 10, (matrix_size, matrix_size), dtype = int)
                break
            else:
                print('input correct number\n')
                continue
        except ValueError:
            print('Please enter integer number!\n')
            continue
    while True:
        try:
            matrix_calc = int(input('\nChoose one of the options offered below:\n'
            ' 1 - Sum of matrix elements\n 2 - Product of matrix elements\n '
            '3 - Search for an element with a given value, in the matrix\n→ '))
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
            if matrix_calc == 1:
                if rec_or_iter == 1:
                    returned = matrix_sum_rec_index(matrix, matrix_size, matrix_size)
                else:
                    returned = matrix_sum_iter(matrix)
                print('\nMatrix ↓\n{}\nSum elements of this matrix → {}\n'
                      .format(matrix, returned))
                break
            elif matrix_calc == 2:
                if rec_or_iter == 1:
                    returned = matrix_mult_rec_index(matrix, matrix_size, matrix_size)
                else:
                    returned = matrix_mult_iter(matrix)
                print('\nMatrix ↓\n{}\nMultiplication elements of this matrix → {}\n'
                      .format(matrix, returned))
                break
            elif matrix_calc == 3:
                s_elem = int(input('\nPlease enter what element you want search → '))
                if rec_or_iter == 1:
                    matrix_search_elem_rec(0, 0, s_elem, matrix)
                    print('\nMatrix ↓\n{}\nElement {} was found at [{}][{}] position'
                          .format(matrix, s_elem, c1, c2))
                else:
                    print('\nMatrix ↓\n{}\nElement {} was found at {} position'
                          .format(matrix, s_elem, matrix_search_elem_iter(matrix, s_elem)))
                break
            else:
                print('input correct number\n')
                continue
        except ValueError:
            print('Please enter integer number!\n')
            continue
    ask = input('\nDo you want to try again? [1/0]: ')
    if ask == '1':
        print()
        continue
    else:
        break
