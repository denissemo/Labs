# Семенов Денис КНІТ 16-А
"""Условие: алгоритмы сортировки"""

import numpy as np

def bubble_sort(n, a):
    """Пузырьковая сортировка.
    
    Параметры: 
        n -- длина массива
        a -- массив, который необходимо отсортировать
    """
    flag = True
    for i in range(1, n):
        if flag:
            flag = False
            for j in range(n - 1, i - 1, -1):
                if a[j - 1] > a[j]:
                    a[j], a[j - 1] = a[j - 1], a[j]
                    flag = True
        else:
            break


def selection_sort(n, a):
    """Сортировка выбором.

    Параметры: 
        n -- длина массива
        a -- массив, который необходимо отсортировать
    """
    for i in range(n):
        min = i  # минимальный елемент
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]


def insertion_sort(n, a):
    """Сортировка вставками.

    Параметры: 
        n -- длина массива
        a -- массив, который необходимо отсортировать
    """
    for i in range(n):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1


def cocktail_sort(n, a):
    """Сортировка перемешиванием.

    Параметры: 
        n -- длина массива
        a -- массив, который необходимо отсортировать
    """
    for k in range(n - 1, 0, -1):
        flag = False
        for i in range(k, 0, -1):  # проход справа налево
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                flag = True
        for i in range(k):  # проход слева направо
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                flag = True
        if not flag:
            return a


def shell_Sort(n, a):
    """Сортировка Шелла.

    Параметры: 
        n -- длина массива
        a -- массив, который необходимо отсортировать
    """
    d = n // 2  # делит последовательность пополам
    while d > 0:
        for i in range(d, n, d):
            j = i
            while j > 0 and a[j] < a[j - d]:
                a[j], a[j - d] = a[j - d], a[j]
                j -= d
        d //= 2


def heap_sort(a):
    """Пирамидальная сортировка.

    Параметры:
        a -- массив, который необходимо отсортировать    
    """

    def swap(parent, child):
        """Потомок и родительский элементы меняются местами.

        Параметры: 
            child -- потомок родительского элемента 
            parent -- родительский элемент
        """
        if a[parent] < a[child]:
            a[parent], a[child] = a[child], a[parent]

    def max_child(left, right):
        """Возвращает индекс наибольшего потомка.

        Параметры:
            left -- левый потомок
            right -- правый потомок
        """
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


while True:
    try:
        fill_ask = int(input('How way you want fill array?\n 1 - Manually\n 2 -'
        ' Randomly\n→ '))
        if fill_ask not in range(1, 3):
            print('Please enter correct number!\n')
            continue
    except ValueError:
        print('Please enter integer number!\n')
        continue
    if fill_ask == 1:
        try:
            l_arr = int(input('Enter length of array: '))
            if l_arr < 1:
                print('Please enter correct number!\n')
                continue
        except ValueError:
            print('Please enter integer number!\n')
            continue
        array = np.zeros(l_arr, dtype = int)
        for i in range(l_arr):
            array[i] = int(input('Input element of array {} → '.format(i + 1)))
    else:
        try:
            l_arr = int(input('Enter length of array: '))
            if l_arr < 1:
                print('Please enter correct number!\n')
                continue
        except ValueError:
            print('Please enter integer number!\n')
            continue
        array = np.random.randint(1, 100, l_arr)
    print('\nSource array:\n', array, '\n')
    while True:
        print('Which sort method you want to use?\n', '1 - Bubble sort\n', '2'
              ' - Selection sort\n', '3 - Insertion sort\n', '4 - Cocktail sort\n'
              , '5 - Shell sort\n', '6 - Heap sort\n')
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
        bubble_sort(l_arr, array)
    elif sort_m == 2:
        selection_sort(l_arr, array)
    elif sort_m == 3:
        insertion_sort(l_arr, array)
    elif sort_m == 4:
        cocktail_sort(l_arr, array)
    elif sort_m == 5:
        shell_Sort(l_arr, array)
    elif sort_m == 6:
        heap_sort(array)
    try:
        sort_direction = int(input('\nIn which order you want to sort the array: \n '
        '1 - Ascending\n 2 - Decrease\n→ '))
        if sort_direction not in range(1, 3):
            print('Please enter correct number!\n')
    except ValueError:
        print('Please enter integer number!\n')
        continue
    if sort_direction == 1:
        print('\nSorted array:\n', array)
    else:
        print('\nSorted array:\n', array[::-1])
    ask = input('\nDo you want to try sort array again? [1/0]: ')
    if ask == '1':
        print()
        continue
    else:
        break
