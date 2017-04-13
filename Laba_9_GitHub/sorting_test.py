# Семенов Денис КНІТ 16-А
"""программа для теста алгоритмов"""

from time import time

def bubble_sort(n, a):
    flag = True
    for i in range(1, n):
        if flag:
            flag = False
            for j in range(n - 1, i - 1, -1):
                if a[j - 1] > a[j]:
                    min = a[j]
                    a[j], a[j - 1] = a[j - 1], min
                    flag = True
        else:
            break


def selection_sort(n, a):
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]


def insertion_sort(n, a):
    for i in range(n):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1


def cocktail_sort(n, a):
    for k in range(n - 1, 0, -1):
        flag = False
        for i in range(k, 0, -1):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                flag = True
        for i in range(k):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                flag = True
        if not flag:
            return a


def shell_Sort(n, a):
    d = n // 2
    while d > 0:
        for i in range(d, n):
            tmp = a[i]
            j = i
            while j > 0 and tmp < a[j - d]:
                a[j] = a[j - d]
                j -= d
            a[j] = tmp
        d //= 2


def swap(i, j, a):
    a[i], a[j] = a[j], a[i]

def heapify(end, i, a):
    l = 2 * i + 1
    r = 2 * (i + 1)
    max = i
    if l < end and a[i] < a[l]:
        max = l
    if r < end and a[max] < a[r]:
        max = r
    if max != i:
        swap(i, max, array)
        heapify(end, max, array)

def heap_sort(n):
    end = n
    start = end // 2 - 1
    for i in range(start, -1, -1):
        heapify(end, i, array)
    for i in range(end-1, 0, -1):
        swap(i, 0, array)
        heapify(i, 0, array)


while True:
    file = open('py_alg.txt')
    a = file.read()
    array = a.split(',')
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
        bubble_sort(10000, array)
        print('\nSorted array: ', array)
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
    elif sort_m == 2:
        s_t = time()
        selection_sort(10000, array)
        print('\nSorted array: ', array)
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
    elif sort_m == 3:
        s_t = time()
        insertion_sort(10000, array)
        print('\nSorted array: ', array)
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
    elif sort_m == 4:
        s_t = time()
        cocktail_sort(10000, array)
        print('\nSorted array: ', array)
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
    elif sort_m == 5:
        s_t = time()
        shell_Sort(10000, array)
        print('\nSorted array: ', array)
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
    elif sort_m == 6:
        s_t = time()
        heap_sort(10000)
        print('\nSorted array: ', array)
        p_t = time() - s_t
        print('\nTime of algorithm execution {:f} second'.format(p_t))
    ask = input('\nDo you want to try sort array again? [y/n]: ').lower()
    if ask == 'y':
        print()
        continue
    else:
        break
