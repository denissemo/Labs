# Семенов Денис КНІТ 16-А
"""Условие: Дан некоторый текст, за которым следует точка (в сам текст точка не
входит). Определить программно, является ли текст правильной записью
«формулы», которая записана в соответствии с синтаксисом EBNF:
Формула = Цифра {Цифра} | (Формула Знак Формула).
Знак = '+' | '-' | '*'.
Цифра = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'."""

import operator as op
import re

def user_input_analyzer(str_f):
    """ Анализирует ввод пользователя на правильность записи формулы.
    А именно, чтоб между символами были пробелы и чтобы выражение было 
    записано в скобках.
    
    :param str_f: исходная строка (формула)
    :return: True или False, в зависимости от правильности ввода
    """
    sign = '*+-'
    if str_f.startswith('(') and str_f.endswith(')'):
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


# парсер формулы
signs = {'+': 0, '-': 0, '*': 1}
op_for_signs = {'+': op.add, '-': op.sub, '*': op.mul}

def innermost_parser(str_f):
    """ Возвращает текст внутри самой внутренней скобки.
    Например: innermost_parser('5 + (4 * (1 * 2))')
    >> '1 * 2'
     
    :param str_f: исходная строка (формула) 
    """
    if '(' not in str_f and ')' not in str_f:
        return str_f
    open = str_f.index('(')
    close = str_f.rindex(')')
    return innermost_parser(str_f[open + 1:close])


def infix_eval(expr):
    """ Сокращенная инфиксная функция eval, работает только с 2 числами.
    Например: 
    infix_eval('2 + 2') 
     >> 2.0
    infix_eval('1 + 2 * (2 * 5)')
     >> ValueError
     
    :param expr: выражение, которое находится в самой внутренней скобке 
    :return: результат вычисления в виде float
    """
    a, oper, b = expr.split()
    return op_for_signs[oper](float(a), float(b))


def full_eval(expr):
    """Вычисляет значения по правилам функции eval, начиная с внутренней 
    скобки.
    Например: full_eval((5 + (4 * (1 * 2))))
    >> 13.0
    
    :param expr: исходная строка (формула)
    :return: новое выражение
    """
    if len(expr.split(' ')) == 1:
        return float(expr)
    inn = innermost_parser(expr)
    new_expr = expr.replace('(' + str(inn) + ')', str(infix_eval(inn)))
    return full_eval(new_expr)


while True:
    formula = input('Please enter formula like this EBNF description:\n'
                    'Formula = Number{Number}|(Formula Sign Formula).\n'
                    "Sign = '+'|'-'|'*'.\nNumber = '0'|'1'|'2'|'3'|'4'|'5'|'6'|"
                    "'7'|'8'|'9'.\n→ ")
    if user_input_analyzer(formula[:-1]) is True:
        pass
    else:
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
        returned = formula_analyzer_rec(formula[1:])
    else:
        returned = formula_analyzer_iter(formula[1:])
    if returned is None:
        print('Unfortunately error, please check your input of formula\n')
        continue
    elif returned[0] is True:
        try:
            evaller = (lambda expr: full_eval(expr))
            result = evaller(formula[:-1])
        except ValueError:
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
