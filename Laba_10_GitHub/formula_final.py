# Семенов Денис КНІТ 16-А
"""Условие: Дан некоторый текст, за которым следует точка (в сам текст точка не
входит). Определить программно, является ли текст правильной записью
«формулы», которая записана в соответствии с синтаксисом EBNF:
Формула = Цифра {Цифра} | (Формула Знак Формула).
Знак = '+' | '-' | '*'.
Цифра = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'."""

import re

def user_input_analyzer(str_f):
    """ Анализирует ввод пользователя на правильность записи формулы.
    А именно, чтоб между символами были пробелы.

    :param str_f: исходная строка (формула)
    :return: True или False, в зависимости от правильности ввода
    """
    sign = '*+-'
    amt_s = 0
    for i in range(len(str_f)):
        for j in range(len(sign)):
            if str_f[i] == sign[j]:
                amt_s += 1
    find_s = re.findall(' [*+-] ', str_f)
    if amt_s == len(find_s):
        return True
    else:
        return False


def formula_analyzer_rec(str_f):
    """ Анализирует формулу на соблюдения синтаксиса EBNF. Рекурсивно.

    :param str_f: исходня строка (формула)
    :return: True или False, + описание ошибки (если есть) 
    """
    if str_f and str_f[0].isdigit() or str_f[0] == '(':
        if str_f[-1] == '.':
            if '(' in str_f:
                str_f = str_f.replace('(', '')
            elif ')' in str_f:
                str_f = str_f.replace(')', '')
            str_f = str_f.lstrip(' 0 1 2 3 4 5 6 7 8 9 ')
            if not str_f or str_f == '.':
                return True, 'Excellent\nFormula is correct!\n'
            if str_f[0] in '+-*':
                return formula_analyzer_rec(str_f[2:])
            else:
                return False, 'Error writing the formula\nSign are not supported!\n'
        else:
            return False, 'Error writing the formula\nYou don`t put the point at the end!\n'
    else:
        return False, 'Error writing the formula\nYou wrote the letter in formula!\n'


def formula_analyzer_iter(str_f):
    """ Анализирует формулу на соблюдения синтаксиса EBNF. Итерационно.

    :param str_f: исходня строка (формула)
    :return: True или False, + описание ошибки (если есть)
    """
    sign = '*+-'
    if str_f[0].isdigit() or str_f[0] == '(':
        if str_f[-1] == '.':
            str_f = str_f[:-1]
            if '(' in str_f:
                str_f = str_f.replace('(', '')
            elif ')' in str_f:
                str_f = str_f.replace(')', '')
            for i in range(0, len(str_f), 2):
                if not str_f[i].isdigit():
                    if str_f[i] in sign:
                        continue
                    return False, 'Error writing the formula\nYou wrote the letter in formula!' \
                                  ' Or sign are not supported!\n'
            return True, 'Excellent\nFormula is correct!\n'
        else:
            return False, 'Error writing the formula\nYou don`t put the point at the end!\n'


signs = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y), '*':
    (2, lambda x, y: x * y)}


def full_eval(str):
    """ Главная функция.
    
    :param str: исходная строка (формула)
    :return: результат вычисления
    """
    def parser(str_f):
        """ Розбирает строку, и записывает числа в стек.
        
        :param str_f: исходная строка (формула)
        :return: число в float формате
        """
        number = ''
        for s in str_f:
            if s in '1234567890.':
                number += s
            elif number:
                yield float(number)
                number = ''
            if s in signs or s in '()':
                yield s
        if number:
            yield float(number)

    def shunting_yard(parsed_formula):
        """ Алгоритм сортировочной станции.
        
        :param parsed_formula: формкула в инфиксной нотации
        :return: числа и операторы в польской нотации
        """
        stack = []
        for token in parsed_formula:
            if token in signs:
                while stack and stack[-1] != '(' and signs[token][0] <= signs[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ')':
                # если элемент - закрывающая скобка, выдаём все элементы из
                # стека, до открывающей скобки,
                # а открывающую скобку выкидываем из стека.
                while stack:
                    x = stack.pop()
                    if x == '(':
                        break
                    yield x
            elif token == '(':
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    def calc(polish):
        """ Получает на вход итерируемый объект чисел и операторов.
        
        :param polish: числа и операторы в польской нотации
        :return: результат вычисления
        """
        stack = []
        for token in polish:
            if token in signs:
                y, x = stack.pop(), stack.pop()
                stack.append(signs[token][1](x, y))
            else:
                stack.append(token)
        return stack[0]

    return calc(shunting_yard(parser(str)))


while True:
    formula = input('Please enter formula like this EBNF description:\n'
                    'Formula = Number{Number}|(Formula Sign Formula).\n'
                    "Sign = '+'|'-'|'*'.\nNumber = '0'|'1'|'2'|'3'|'4'|'5'|'6'|"
                    "'7'|'8'|'9'.\n→ ")
    if user_input_analyzer(formula[:-1]) is False:
        print('Please write a space before and after the Sign. And try again.\n'
              'If you did this, check your formula with EBNF.\n')
        continue
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
    if rec_or_iter == 1:
        returned = formula_analyzer_rec(formula)
    else:
        returned = formula_analyzer_iter(formula)
    if returned is None:
        print('Unfortunately error, please check your input of formula\n')
        continue
    elif returned[0] is True:
        try:
            result = full_eval(formula[:-1])
        except (IndexError, ValueError):
            print('Ohh it looks like you did not correctly write a formula, the'
            ' function can only count two numbers. Please try again.\n')
            continue
        print(returned[1])
        print('Now we will calculate the result of formula ↓')
        print('\nThe result of formula {} is → {}\n'.format(formula, result))
    elif returned[0] is False:
        print(returned[1])
        continue
    ask = input('Do you want to try again? [1/0]: ')
    if ask == '1':
        print()
        continue
    else:
        break

