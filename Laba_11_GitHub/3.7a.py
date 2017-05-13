# Семенов Денис КНІТ 16-А
""" Условие: Дан файл f, компоненты которого являются целыми числами. Записать в
файл g все четные числа файла f, а в файл h – все нечетные. Порядок следования
чисел сохранить."""

import numpy as np

while True:
    try:
        l_arr = int(input('Please enter the amount of numbers to write to file f\n→ '))
        if l_arr < 1:
            print('Amount must be bigger!\n')
            continue
    except ValueError:
        print('Please enter integer number!\n')
        continue
    a_numb = np.random.randint(1, 100, l_arr)
    file_numb = open('f.txt', 'w')
    for i in range(len(a_numb)):
        file_numb.write(str(a_numb[i]) + ' ')
    file_numb.close()
    file = open('f.txt')
    g = open('g.txt', 'w')  # четные числа
    h = open('h.txt', 'w')  # нечетные числа
    f = file.read()
    f = f[:-1].split(' ')
    for i in f:
        if int(i) % 2 == 0:
            print('Write even number {} to file g.txt'.format(i))
            g.write(i + ' ')
        else:
            print('Write odd number {} to file h.txt'.format(i))
            h.write(i + ' ')
    file.close()
    g.close()
    h.close()
    ask = input('\nDo you want try again? [1/0]: ')
    if ask == '1':
        continue
    else:
        break
