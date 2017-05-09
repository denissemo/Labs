# Семенов Денис КНІТ 16-А
"""программа для теста алгоритмов"""

import numpy as np
from time import time


def bubble_sort(n, a, c):
    """ Пузырьковая сортировка.
    
    :param n: длина массива
    :param a: массив, который необходимо отсортировать
    :param c: выбор направления сортировки
    :return: число сравнений и перестановок элементов
    """
    flag = True
    c1 = 0
    c2 = 0
    for i in range(1, n):
        if flag:
            flag = False
            for j in range(n - 1, i - 1, -1):
                c1 += 1
                if c == 1:
                    if a[j - 1] > a[j]:
                        a[j], a[j - 1] = a[j - 1], a[j]
                        c2 += 1
                        flag = True
                elif c == 2:
                    if a[j - 1] < a[j]:
                        a[j], a[j - 1] = a[j - 1], a[j]
                        c2 += 1
                        flag = True
        else:
            break
    return c1, c2


def selection_sort(n, a, c):
    """ Сортировка выбором.
    
    :param n: длина массива
    :param a: массив, который необходимо отсортировать
    :param c: выбор направления сортировки
    :return: число сравнений и перестановок элементов
    """
    c1 = 0
    c2 = 0
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            c1 += 1
            if c == 1:
                if a[j] < a[min]:
                    min = j
            elif c == 2:
                if a[j] > a[min]:
                    min = j
        a[i], a[min] = a[min], a[i]
        c2 += 1
    return c1, c2


def insertion_sort(n, a, c):
    """ Сортировка вставками.
    
    :param n: длина массива
    :param a: массив, который необходимо отсортировать
    :param c: выбор направления сортировки
    :return: число сравнений и перестановок элементов
    """
    c1 = 0
    c2 = 0
    for i in range(n):
        j = i
        c1 += 1
        if c == 1:
            while j > 0 and a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
                c2 += 1
                j -= 1
        elif c == 2:
            while j > 0 and a[j] > a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
                c2 += 1
                j -= 1
    return c1, c2


def cocktail_sort(n, a, c):
    """ Сортировка перемешиванием.
    
    :param n: длина массива
    :param a: массив, который необходимо отсортировать
    :param c: выбор направления сортировки
    :return: число сравнений и перестановок элементов
    """
    c1 = 0
    c2 = 0
    for k in range(n - 1, 0, -1):
        flag = False
        for i in range(k, 0, -1):
            c1 += 1
            if c == 1:
                if a[i] < a[i - 1]:
                    a[i], a[i - 1] = a[i - 1], a[i]
                    c2 += 1
                    flag = True
            elif c == 2:
                if a[i] > a[i - 1]:
                    a[i], a[i - 1] = a[i - 1], a[i]
                    c2 += 1
                    flag = True
        for i in range(k):
            c1 += 1
            if c == 1:
                if a[i] > a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]
                    c2 += 1
                    flag = True
            elif c == 2:
                if a[i] < a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]
                    c2 += 1
                    flag = True
        if not flag:
            return c1, c2


def shell_Sort(n, a, c):
    """ Сортировка Шелла.
    
    :param n: длина массива
    :param a: массив, который необходимо отсортировать
    :param c: выбор направления сортировки
    :return: число сравнений и перестановок элементов
    """
    c1 = 0
    c2 = 0
    d = n // 2  # делит последовательность пополам
    while d > 0:
        for i in range(d, n, d):
            j = i
            c1 += 1
            if c == 1:
                while j > 0 and a[j] < a[j - d]:
                    a[j], a[j - d] = a[j - d], a[j]
                    c2 += 1
                    j -= d
            elif c == 2:
                while j > 0 and a[j] > a[j - d]:
                    a[j], a[j - d] = a[j - d], a[j]
                    c2 += 1
                    j -= d
        d //= 2
    return c1, c2


def heap_sort(a, c):
    """ Пирамидальная сортировка.

    :param a: массив, который необходимо отсортировать
    :param c: выбор направления сортировки
    :return: число сравнений и перестановок элементов
    """
    c1 = 0
    c2 = 0

    def swap(parent, child):
        """ Потомок и родительский элементы меняются местами.
        
        :param parent: родительский элемент
        :param child: потомок родительского элемента
        """
        nonlocal c2
        if c == 1:
            if a[parent] < a[child]:
                c2 += 1
                a[parent], a[child] = a[child], a[parent]
        elif c == 2:
            if a[parent] > a[child]:
                c2 += 1
                a[parent], a[child] = a[child], a[parent]

    def max_child(left, right):
        """ Возвращает индекс наибольшего потомка.
        
        :param left: левый потомок
        :param right: правый потомок
        :return: индекс наибольшего потомка
        """
        nonlocal c1
        c1 += 1
        if a[left] > a[right]:
            if c == 1:
                return left
            elif c == 2:
                return right
        else:
            if c == 1:
                return right
            elif c == 2:
                return left

    def bin_tree(parent, end):
        """ Создает сортировочное дерево.
        
        :param parent: индекс родительского элемента
        :param end: индекс последнего элемента последовательности
        """
        nonlocal c1
        c1 += 1
        while 2 * parent + 2 < end:
            max = max_child(2 * parent + 1, 2 * parent + 2)
            swap(parent, max)
            parent = max

    l = len(a)
    for i in range(l // 2 - 1, -1, -1):  # по очереди перебираются
        bin_tree(i, l)                   # родительские элементы

    for j in range(l - 1, 0, -1):  # сортирует массив
        swap(j, 0)
        bin_tree(0, j)
    return c1, c2

while True:
    while True:
        try:
            test_arr = int(input('What test array do you want to use?\n 1 - Pse'
            'udorandom\n 2 - Sorted in ascending order\n 3 - Sorted in descendi'
            'ng order\n 4 - Manual\n→ '))
            if test_arr in range(1, 5):
                what_arr = ''
                if test_arr == 1:
                    what_arr = 'Random'
                    arr_file = open('test_array_1.txt')  # массив с рандомными числами
                elif test_arr == 2:
                    what_arr = 'Ascending'
                    arr_file = open('test_array_2.txt')  # массив упорядоченный по вохрастанию
                elif test_arr == 3:
                    what_arr = 'Descending'
                    arr_file = open('test_array_3.txt')  # массив упорядоченный по убыванию
                elif test_arr == 4:
                    what_arr = 'Manual'
                    while True:
                        try:
                            l_arr = int(input('Enter length of array: '))
                            if l_arr < 1:
                                print('Please enter correct number!\n')
                                continue
                            break
                        except ValueError:
                            print('Please enter integer number!\n')
                            continue
                    flag = True
                    while flag:
                        file = open('test_array_4.txt', 'w')
                        for i in range(l_arr):
                            inp = input('Input element of array {} → '
                                        .format(i + 1))
                            if inp.isdigit():
                                file.write('{},'.format(inp))
                                flag = False
                            else:
                                print('Please enter integer number!\n')
                                flag = True
                                break
                        if not flag:
                            break
                    file.close()
                    arr_file = open('test_array_4.txt')  # заданый пользователем массив
            else:
                print('Please enter correct number!\n')
                continue
        except ValueError:
            print('Please enter integer number!\n')
            continue
        else:
            break
    a = arr_file.read()
    if a.endswith(','):
        a = a[0: -1]
        array = np.zeros(l_arr, dtype = int)
    else:
        array = np.zeros(10000, dtype = int)  # Тестовый массив
    arr = a.split(',')
    for i in range(len(arr)):
        array[i] = arr[i]
    print('Source array: ', array, '\n')
    print('Which sort method you want to use?\n', '1 - Bubble sort\n', '2'
        ' - Selection sort\n', '3 - Insertion sort\n', '4 - Cocktail sort\n',
          '5 - Shell sort\n', '6 - Heap sort\n')
    while True:
        try:
            sort_m = int(input('Please enter number: '))
            if sort_m not in range(1, 7):
                print('Please enter correct number!\n')
                continue
        except ValueError:
            print('Please enter integer number!\n')
            continue
        else:
            break
    while True:
        try:
            sort_direction = int(
                input('\nIn which order you want to sort the array: \n '
                      '1 - Ascending\n 2 - Decrease\n→ '))
            if sort_direction in range(1, 3):
                if sort_direction == 1:
                    direct = 'Ascending'
                elif sort_direction == 2:
                    direct = 'Decrease'
            else:
                print('Please enter correct number!\n')
                continue
        except ValueError:
            print('Please enter integer number!\n')
            continue
        else:
            break
    if sort_m == 1:
        s_t = time()
        returned = bubble_sort(len(array), array, sort_direction)
        print('Test array: {}\nArray sorted by {} order\n{}'.format(what_arr,
                                                            direct, array))
        print('\nNumber of comparisons: {}\nNumber of exchanges: {}'
              .format(returned[0], returned[1]))
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
        data_file = open('test_data.txt', 'a')
        data_file.write('\nBubble sort:\n Test array: {}\n Sorted by {} order\n'
                        ' time: {}\n comparisons: {}\n exchanges: {}\n'
            .format(what_arr, direct, str(p_t), returned[0], returned[1]))
        data_file.close()
    elif sort_m == 2:
        s_t = time()
        returned = selection_sort(len(array), array, sort_direction)
        print('Test array: {}\nArray sorted by {} order\n{}'.format(what_arr,
                                                            direct, array))
        print('\nNumber of comparisons: {}\nNumber of exchanges: {}'
              .format(returned[0], returned[1]))
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
        data_file = open('test_data.txt', 'a')
        data_file.write('\nSelection sort:\n Test array: {}\n Sorted by {} orde'
                        'r\n time: {}\n comparisons: {}\n exchanges: {}\n'
                        .format(what_arr, direct, str(p_t), returned[0], returned[1]))
        data_file.close()
    elif sort_m == 3:
        s_t = time()
        returned = insertion_sort(len(array), array, sort_direction)
        print('Test array: {}\nArray sorted by {} order\n{}'.format(what_arr,
                                                            direct, array))
        print('\nNumber of comparisons: {}\nNumber of exchanges: {}'
              .format(returned[0], returned[1]))
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
        data_file = open('test_data.txt', 'a')
        data_file.write('\nInsertion sort:\n Test array: {}\n Sorted by {} orde'
                        'r\n time: {}\n comparisons: {}\n exchanges: {}\n'
                        .format(what_arr, direct, str(p_t), returned[0], returned[1]))
        data_file.close()
    elif sort_m == 4:
        s_t = time()
        returned = cocktail_sort(len(array), array, sort_direction)
        print('Test array: {}\nArray sorted by {} order\n{}'.format(what_arr,
                                                            direct, array))
        print('\nNumber of comparisons: {}\nNumber of exchanges: {}'
              .format(returned[0], returned[1]))
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
        data_file = open('test_data.txt', 'a')
        data_file.write('\nCocktail sort:\n Test array: {}\n Sorted by {} orde'
                        'r\n time: {}\n comparisons: {}\n exchanges: {}\n'
                        .format(what_arr, direct, str(p_t), returned[0], returned[1]))
        data_file.close()
    elif sort_m == 5:
        s_t = time()
        returned = shell_Sort(len(array), array, sort_direction)
        print('Test array: {}\nArray sorted by {} order\n{}'.format(what_arr,
                                                            direct, array))
        print('\nNumber of comparisons: {}\nNumber of exchanges: {}'
              .format(returned[0], returned[1]))
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
        data_file = open('test_data.txt', 'a')
        data_file.write('\nShell sort:\n Test array: {}\n Sorted by {} order\n '
                        'time: {}\n comparisons: {}\n exchanges: {}\n'
                        .format(what_arr, direct, str(p_t), returned[0], returned[1]))
        data_file.close()
    elif sort_m == 6:
        s_t = time()
        returned = heap_sort(array, sort_direction)
        print('Test array: {}\nArray sorted by {} order\n{}'.format(what_arr,
                                                            direct, array))
        print('\nNumber of comparisons: {}\nNumber of exchanges: {}'
              .format(returned[0], returned[1]))
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
        data_file = open('test_data.txt', 'a')
        data_file.write('\nHeap sort:\n Test array: {}\n Sorted by {} order\n t'
                        'ime: {}\n comparisons: {}\n exchanges: {}\n'
                        .format(what_arr, direct, str(p_t), returned[0], returned[1]))
        data_file.close()
    ask = input('\nDo you want to try sort array again? [1/0]: ')
    if ask == '1':
        print()
        continue
    else:
        arr_file.close()
        break
