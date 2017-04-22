# Семенов Денис КНІТ 16-А
"""программа для теста алгоритмов"""

import numpy as np
from time import time


def bubble_sort(n, a):
    """Пузырьковая сортировка.

    Параметры: 
        n -- длина массива
        a -- массив, который необходимо отсортировать
    """
    flag = True
    c1 = 0
    c2 = 0
    for i in range(1, n):
        if flag:
            flag = False
            for j in range(n - 1, i - 1, -1):
                c1 += 1
                if a[j - 1] > a[j]:
                    a[j], a[j - 1] = a[j - 1], a[j]
                    c2 += 1
                    flag = True
        else:
            break
    return c1, c2


def selection_sort(n, a):
    """Сортировка выбором.

    Параметры: 
        n -- длина массива
        a -- массив, который необходимо отсортировать
    """
    c1 = 0
    c2 = 0
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            c1 += 1
            if a[j] < a[min]:
                min = j
        c2 += 1
        a[i], a[min] = a[min], a[i]
    return c1, c2


def insertion_sort(n, a):
    """Сортировка вставками.

    Параметры: 
        n -- длина массива
        a -- массив, который необходимо отсортировать
    """
    c1 = 0
    c2 = 0
    for i in range(n):
        j = i
        c1 += 1
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            c2 += 1
            j -= 1
    return c1, c2


def cocktail_sort(n, a):
    """Сортировка перемешиванием.

    Параметры: 
        n -- длина массива
        a -- массив, который необходимо отсортировать
    """
    c1 = 0
    c2 = 0
    for k in range(n - 1, 0, -1):
        flag = False
        for i in range(k, 0, -1):
            c1 += 1
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                c2 += 1
                flag = True
        for i in range(k):
            c1 += 1
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                c2 += 1
                flag = True
        if not flag:
            return c1, c2


def shell_Sort(n, a):
    """Сортировка Шелла.

    Параметры: 
        n -- длина массива
        a -- массив, который необходимо отсортировать
    """
    c1 = 0
    c2 = 0
    d = n // 2  # делит последовательность пополам
    while d > 0:
        for i in range(d, n, d):
            j = i
            c1 += 1
            while j > 0 and a[j] < a[j - d]:
                a[j], a[j - d] = a[j - d], a[j]
                c2 += 1
                j -= d
        d //= 2
    return c1, c2


def heap_sort(a):
    """Пирамидальная сортировка.

    Параметры:
        a -- массив, который необходимо отсортировать    
    """
    c1 = 0
    c2 = 0

    def swap(parent, child):
        """Потомок и родительский элементы меняются местами.

        Параметры: 
            child -- потомок родительского элемента 
            parent -- родительский элемент
        """
        if a[parent] < a[child]:
            nonlocal c2
            c2 += 1
            a[parent], a[child] = a[child], a[parent]

    def max_child(left, right):
        """Возвращает индекс наибольшего потомка.

        Параметры:
            left -- левый потомок
            right -- правый потомок
        """
        nonlocal c1
        c1 += 1
        if a[left] > a[right]:
            return left
        else:
            return right

    def bin_tree(parent, end):
        """Создает сортировочное дерево.

        Параметры: 
            parent -- индекс родительского элемента
            end -- индекс последнего элемента последовательности
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
    arr_file = open('test_array.txt')
    a = arr_file.read()
    array = np.zeros(10000, dtype = int)  # Тестовый массив 10000 случайных целых чисел
    arr = a.split(',')
    for i in range(len(arr)):
        array[i] = arr[i]
    print('Source array: ', array, '\n')
    print('Which sort method you want to use?\n', '1 - Bubble sort\n', '2'
        ' - Selection sort\n', '3 - Insertion sort\n', '4 - Cocktail sort\n'
        , '5 - Shell sort\n', '6 - Heap sort\n')
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
    if sort_m == 1:
        s_t = time()
        returned = bubble_sort(10000, array)
        print('\nSorted array: ', array)
        print('\nNumber of comparisons: {}\nNumber of exchanges: {}'
              .format(returned[0], returned[1]))
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
        data_file = open('test_data.txt', 'a')
        data_file.write('\nBubble sort:\n time: {}\n comparisons: {}\n exchange'
                        's: {}\n'.format(str(p_t), returned[0], returned[1]))
        data_file.close()
    elif sort_m == 2:
        s_t = time()
        returned = selection_sort(10000, array)
        print('\nSorted array: ', array)
        print('\nNumber of comparisons: {}\nNumber of exchanges: {}'
              .format(returned[0], returned[1]))
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
        data_file = open('test_data.txt', 'a')
        data_file.write('\nSelection sort:\n time: {}\n comparisons: {}\n excha'
                        'nges: {}\n'.format(str(p_t), returned[0], returned[1]))
        data_file.close()
    elif sort_m == 3:
        s_t = time()
        returned = insertion_sort(10000, array)
        print('\nSorted array: ', array)
        print('\nNumber of comparisons: {}\nNumber of exchanges: {}'
              .format(returned[0], returned[1]))
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
        data_file = open('test_data.txt', 'a')
        data_file.write('\nInsertion sort:\n time: {}\n comparisons: {}\n excha'
                        'nges: {}\n'.format(str(p_t), returned[0], returned[1]))
        data_file.close()
    elif sort_m == 4:
        s_t = time()
        returned = cocktail_sort(10000, array)
        print('\nSorted array: ', array)
        print('\nNumber of comparisons: {}\nNumber of exchanges: {}'
              .format(returned[0], returned[1]))
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
        data_file = open('test_data.txt', 'a')
        data_file.write('\nCocktail sort:\n time: {}\n comparisons: {}\n exchan'
                        'ges: {}\n'.format(str(p_t), returned[0], returned[1]))
        data_file.close()
    elif sort_m == 5:
        s_t = time()
        returned = shell_Sort(10000, array)
        print('\nSorted array: ', array)
        print('\nNumber of comparisons: {}\nNumber of exchanges: {}'
              .format(returned[0], returned[1]))
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
        data_file = open('test_data.txt', 'a')
        data_file.write('\nShell sort:\n time: {}\n comparisons: {}\n exchanges'
                        ': {}\n'.format(str(p_t), returned[0], returned[1]))
        data_file.close()
    elif sort_m == 6:
        s_t = time()
        returned = heap_sort(array)
        print('\nSorted array: ', array)
        print('\nNumber of comparisons: {}\nNumber of exchanges: {}'
              .format(returned[0], returned[1]))
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
        data_file = open('test_data.txt', 'a')
        data_file.write('\nHeap sort:\n time: {}\n comparisons: {}\n exchanges'
                        ': {}\n'.format(str(p_t), returned[0], returned[1]))
        data_file.close()
    ask = input('\nDo you want to try sort array again? [1/0]: ')
    if ask == '1':
        print()
        continue
    else:
        arr_file.close()
        break
