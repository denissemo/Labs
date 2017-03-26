# Семенов Денис КНІТ 16-А

import elizabeth as el
import random as rnd
from enum import Enum

class eyes(Enum):
    # класс с цветами глаз
    синий = 1
    голубой = 2
    серый = 3
    зеленый = 4
    болотный = 5
    карий = 6
    черный = 7

def db_input():
    print('\nКак Вы хотите вводить информацию в БД: вручную или рандомно? [1/2]')
    while True:
        try:
            ask_inp = int(input('Выберите цифру → '))
            if ask_inp not in range(1, 3):
                print('Пожалуйста, введите корректные данные ☻\n')
                continue
            break
        except ValueError:
            print('Пожалуйста, введите целое число ☻\n')
            continue
    return ask_inp

def db_manual_rnd_input(x):
    while True:
        try:
            t_num = int(input('\nВведите количество туристов → '))
        except ValueError:
            print('Пожалуйста, введите целое число ☻\n')
            continue
        if t_num < 1:
            print('Слишком мало людей...\n')
            continue
        else:
            inform = [[] * 1 for i in range(t_num)]
            if x == 1:
                # ручной ввод данных
                for i in range(t_num):
                    while True:
                        surname = input(
                            '\nВведите фамилию туриста → ').capitalize()
                        if surname.isalpha():
                            inform[i].append(surname)
                            break
                        else:
                            print('Фамилия не может состоять из цифр!\n')
                            continue
                    while True:
                        try:
                            age = int(
                                input('\nВведите возраст туриста [10,55] → '))
                            if age not in range(10, 56):
                                print(
                                    'Пожалуйста, введите корректный возраст ☻\n')
                                continue
                            inform[i].append(str(age))
                            break
                        except ValueError:
                            print('Пожалуйста, введите целое число ☻\n')
                            continue
                    while True:
                        gender = input('\nВведите пол туриста [м/ж] → ').lower()
                        if gender == 'м':
                            inform[i].append('мужской')
                            break
                        elif gender == 'ж':
                            inform[i].append('женский')
                            break
                        else:
                            print('Пожалуйста, введите пол человека ☻\n')
                            continue
                    print()
                    for j in range(1, 7):
                        print(eyes(j).name, end = ' → ')
                        print(eyes(j).value, end = ';  ')
                    while True:
                        try:
                            eye = int(
                                input('\n\nВыберите цвет глаз туриста, каждый'
                                      ' цвет обозначеный номером → '))
                            if eye not in range(1, 8):
                                print(
                                    'Пожалуйста, введите корректные данные ☻\n')
                                continue
                            inform[i].append(str(eyes(eye).name))
                            break
                        except ValueError:
                            print('Пожалуйста, введите целое число ☻\n')
                            continue
            elif x == 2:
                # рандомный ввод данных
                for i in range(t_num):
                    pers = el.Personal('ru')
                    gender = 'male', 'female'
                    rand = rnd.choice(gender)
                    inform[i].append(pers.surname(rand))
                    inform[i].append(str(pers.age(10, 55)))
                    if rand == 'male':
                        inform[i].append('мужской')
                    else:
                        inform[i].append('женский')
                    inform[i].append(str(eyes(rnd.randint(1, 7)).name))
        inform.sort()
        print('\nГотово, данные внесены; посмотреть их Вы можете на главной страннице\n')
        return inform

def db_see():
    try:
        print('\n{:^80}'.format('База данных туристов'))
        print('╔' + '═' * 89 + '╗')
        print('║{:^20}║{:^16}║{:^20}║{:^19}║'.format('Имя', 'Возраст', 'Пол',
                                                     'Цвет глаз'))
        print('╚' + '═' * 89 + '╝')
        for i in returned:
            print('+' + '-' * 78 + '+')
            print('|{:^20}|{:^16}|{:^20}|{:^19}|'.format(i[0], i[1], i[2], i[3]))
        print('+' + '-' * 78 + '+')
    except NameError:
        print('\nВ БД пока нет информации :(\nВы можете внести её прямо сейчас...\n')

def arith_mean(lst):
    return float(sum(lst)) / len(lst)

def db_stat():
    try:
        print('\n{:^80}\n{:^80}\n{} {:^27}{:^27}'.format('Здесь вы можете увидеть '
        'количество туристов по заданых параметрах', 'А именно:', '(1) по задан'
        'ому возрасту', '(2) по заданому цвету глаз', '(3) вывести среднестатистические данные'))
        while True:
            try:
                ask = int(input('Выберите цифру → '))
                if ask not in range(1, 4):
                    print('Пожалуйста, введите корректные данные ☻\n')
                    continue
                break
            except ValueError:
                print('Пожалуйста, введите целое число ☻\n')
                continue
        l_m = []
        l_w = []
        if ask == 1:
            while True:
                try:
                    age = int(input('\nВведите возраст туриста [10,55] → '))
                    if age not in range(10, 56):
                        print('Пожалуйста, введите корректный возраст ☻\n')
                        continue
                    age = str(age)
                    for i in returned:
                        if i[1] == age:
                            if i[2] == 'мужской':
                                l_m.append(i[1])
                            else:
                                l_w.append(i[1])
                    print('\nКоличество мужчин заданого возраста:', len(l_m))
                    print('Количество женщин заданого возраста:', len(l_w))
                    break
                except ValueError:
                    print('Пожалуйста, введите целое число ☻\n')
                    continue
        elif ask == 2:
            while True:
                try:
                    print()
                    for j in range(1, 7):
                        print(eyes(j).name, end = ' → ')
                        print(eyes(j).value, end = ';  ')
                    eye = int(input('\n\nВыберите цвет глаз туриста, каждый'
                                    ' цвет обозначеный номером → '))
                    if eye not in range(1, 8):
                        print('Пожалуйста, введите корректные данные ☻\n')
                        continue
                    eye = eyes(eye).name
                    for i in returned:
                        if i[3] == eye:
                            if i[2] == 'мужской':
                                l_m.append(i[1])
                            else:
                                l_w.append(i[1])
                    print('\nКоличество мужчин с заданым цветом глаз:', len(l_m))
                    print('Количество женщин c заданым цветом глаз:', len(l_w))
                    break
                except ValueError:
                    print('Пожалуйста, введите целое число ☻\n')
                    continue
        elif ask == 3:
            stat_age = []
            for i in returned:
                i[1] = int(i[1])
                stat_age.append(i[1])
                if i[2] == 'мужской':
                    l_m.append('0')
                else:
                    l_w.append('1')
            print('\nСреднестатистический возраст туристов: ', arith_mean(stat_age))
            print('\nМужчин {}%'.format(len(l_m) * len(returned) / 100))
            print('Женщин {}%'.format(len(l_w) * len(returned) / 100))
    except NameError:
        print('\nВ БД пока нет информации :(\nВы можете внести её прямо сейчас...\n')


def main_menu():
    print()
    print('*' * 80)
    print('|{:^78}|\n|{:^77} |'.format('Приветствую Вас в этой замечательной програ'
    'мме!', 'Это база данных, хранящая информацию о туристах'))
    print('|{:^77}|'.format('▼Вы можете выбрать один из вариантов предложеных ниже▼'))
    print('*' * 80)
    print('|{:^25}|{:^25}|{:^26}|\n|{:^25}|{:^25}|{:^26}|\n|{:^25}|{:^25}|{:^26}|'
          .format('Ввести', 'Вывести', 'Вывести количество', 'данные в БД', 'БД на '
          'экран', 'мужчин и женщин', '(1)', '(2)', '(3)'))
    print('*' * 80)

while True:
    main_menu()
    try:
        db_query = int(input('Пожалуйста, сделайте Ваш выбор → '))
        if db_query == 1:
            returned = db_manual_rnd_input(db_input())
        elif db_query == 2:
            db_see()
        elif db_query == 3:
            db_stat()
        else:
            print('Пожалуйста, введите корректные данные ☻\n')
            continue
    except ValueError:
        print('Пожалуйста, введите целое число ☻\n')
        continue
    ask = input('\nЕсли Вы хотите вернуться на главную странницу нажмите кнопку [y]'
    ', иначе произойдет выход из программы :( ').lower()
    if ask == 'y':
        continue
    else:
        break
