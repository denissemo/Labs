# Семенов Денис КНІТ 16-А
"""Условие: Напишите программу создания на системном диске в каталоге NewFold
своего каталога, в нем текстового файла со своей анкетой и сформируйте код
программного вывода файла с анкетой на экран монитора."""

import os
from elizabeth import Personal, Address
from random import choice


def rand_inp(f):
    """ Заполняет анкету случайными данными.
    
    :param f: анкета (list)
    """
    sex = 'male', 'female'
    rnd_sex = choice(sex)
    f.append('{:^45}\n'.format('Your Form'))
    f.append('Name: {}\n'.format(Personal('ru').name(rnd_sex)))
    f.append('Surname: {}\n'.format(Personal('ru').surname(rnd_sex)))
    f.append('Age: {}\n'.format(str(Personal('ru').age(16, 60))))
    f.append('Address: {}\n'.format(Address('ru').address()))
    f.append('Phone: {}\n'.format(Personal('uk').telephone()))


def mnl_inp(f):
    """ Данные вносятся вручную в анкету.

    :param f: анкета (list)
    """
    f.append('{:^45}\n'.format('Your Form'))
    f.append('Name: {}\n'.format(input('Please enter your name → ')))
    f.append('Surname: {}\n'.format(input('\nPlease enter your surname → ')))
    while True:
        age = input('\nPlease enter your age [> 16] → ')
        if age.isdigit() and int(age) > 16:
            f.append('Age: {}\n'.format(age))
            break
        else:
            print('Please enter correct age!')
            continue
    f.append('Address: {}\n'.format(input('\nPlease enter your address → ')))
    while True:
        phone = input('\nPlease enter your phone [+code city...] → ')
        if phone.startswith('+') and phone[1:].isdigit():
            f.append('Phone: {}\n'.format(phone))
            break
        else:
            print('Please enter correct phone!')
            continue


def create_catalog(path):
    """ Создает каталог NewFold, и в нем каталог MyForm, в котором 
    создается текстовый файл с анкетой пользователя.
    
    :param path: путь к каталогу
    :return: путь к созданному файлу
    """
    global form
    path = str(path + '\\NewFold\\MyForm\\')
    os.makedirs(path)
    f = form[1][6:].replace('\n', '')
    file = open(path + f + '.txt', 'w')
    file.writelines(form)
    file.close()
    return str(path + f + '.txt')


while True:
    form = []
    print('Now we fill your Form ↓\n')
    rand_or_mnl = input('How you want to fill the Form?\n(1) Randomly\n(2) Manual\n → ')
    if rand_or_mnl == '1':
        rand_inp(form)
    elif rand_or_mnl == '2':
        mnl_inp(form)
    else:
        print('Please try again! You made a mistake.\n')
        continue
    print('Form was successful created.\n')
    while True:
        w_path = input('Where do you want to create the NewFold catalog?\n'
                   '(1) Current directory -- {}\n(2) Choose a path\n → '
                   .format(os.getcwd()))
        if w_path == '1':
            try:
                returned = create_catalog(os.getcwd())
            except FileExistsError:
                print('Directory was created, please choose another path!\n')
                continue
        elif w_path == '2':
            file_path = input('Where you want to save the Form file?\nPlease enter '
            'path like "Name of disk:\\Your path..."\n → ')
            if os.path.exists(file_path):
                returned = create_catalog(file_path)
            else:
                print('Directory not found, please check your path!\n')
                continue
        else:
            print('Please try again! You made a mistake.\n')
            continue
        print('Your Form was successful saved at {}\n'.format(returned))
        break
    while True:
        form_out = input('If you want display the Form enter (1)\n → ')
        if form_out == '1':
            file_display = open(returned, 'r')
            for i in file_display:
                print(i)
            file_display.close()
            break
        else:
            print('Please try again! You made a mistake.\n')
            continue
    ask = input('\nDo you want try again? [1/0]: ')
    if ask == '1':
        continue
    else:
        break
