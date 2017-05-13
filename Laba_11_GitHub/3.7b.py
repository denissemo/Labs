# Семенов Денис КНІТ 16-А
"""Условие: Даны символьные файлы f и g. Записать в файл h все начальные
совпадающие компоненты файлов f и g."""

from random import choice

def cum_sum_drop(seq):
    """ Подсчитывает количество совпадений.
    
    :param seq: список с булевыми переменными
    :return: список с количеством совпадений в строках. 
    Например для строк: 
    s1 = 'aaabcab'; s2 = 'cccbcbb' список будет иметь вид [0,0,0,1,2,0,1]
    """
    sum = 0
    for x in seq:
        sum = (sum + 1) if x else 0
        yield sum


def str_index(csd):
    """ Ищет индексы начальных совпадений.
    
    :param csd: список с количеством совпадений в строках.
    :return: индекс начального и конечного совпадения.
    Например для списка: [0,0,0,1,2,0,1]
    start = 3; end = 5.
    """
    start = 0
    end = 0
    flag = True
    for i in range(len(csd)):
        if csd[i] == 0:
            end = i
            if not flag:
                break
        if flag:
            if csd[i] != 0:
                start = i
                if start != 0:
                    flag = False
    return start, end


while True:
    try:
        l_arr = int(
            input('Please enter the amount of symbols to write to file f and g\n→ '))
        if l_arr < 1:
            print('Amount must be bigger!\n')
            continue
    except ValueError:
        print('Please enter integer number!\n')
        continue
    with open('f.txt', 'w') as file1:
        file1.write(''.join(choice('abc') for l in range(l_arr)))
    with open('g.txt', 'w') as file2:
        file2.write(''.join(choice('abc') for k in range(l_arr)))
    with open('f.txt', 'r') as f_file:
        f = f_file.read()
    with open('g.txt', 'r') as g_file:
        g = g_file.read()
    print(f)
    print(g)
    print('Write at file h')
    with open('h.txt', 'w') as h_file:
        csd_list = list(cum_sum_drop(c1 == c2 for c1, c2 in zip(f, g)))
        returned = str_index(csd_list)
        h_file.write(f[returned[0]:returned[1]])
    ask = input('\nDo you want try again? [1/0]: ')
    if ask == '1':
        continue
    else:
        break
