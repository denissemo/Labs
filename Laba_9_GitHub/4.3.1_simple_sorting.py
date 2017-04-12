# Семенов Денис КНІТ 16-А
"""Условие: простые алгоритмы сортировки"""

import numpy as np

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
            a[j], a[j-1] = a[j-1],a[j]
            j -= 1


while True:
    try:
        l_arr = int(input('Enter length of array: '))
        if l_arr < 1:
            print('Please enter correct number!\n')
            continue
    except ValueError:
        print('Please enter integer number!\n')
        continue
    array = np.random.randint(1, 100, l_arr)
    print('\nSource array: ', array, '\n')
    while True:
        print('Which sort method you want to use?\n', '1 - Bubble sort\n', '2'
              ' - Selection sort\n', '3 - Insertion sort\n')
        try:
            sort_m = int(input('Please enter number: '))
            if sort_m not in range(1, 4):
                print('Please enter correct number!\n')
                continue
        except ValueError:
            print('Please enter integer number!\n')
            continue
        else:
            break
    if sort_m == 1:
        bubble_sort(l_arr, array)
        print('\nSorted array: ', array)
    elif sort_m == 2:
        selection_sort(l_arr, array)
        print('\nSorted array: ', array)
    elif sort_m == 3:
        insertion_sort(l_arr, array)
        print('\nSorted array: ', array)
    ask = input('\nDo you want to try sort array again? [y/n]: ').lower()
    if ask == 'y':
        print()
        continue
    else:
        break
