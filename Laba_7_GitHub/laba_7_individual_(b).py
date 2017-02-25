# Семенов Денис КНІТ 16-А
"""Условие: дана непустая последовательность слов из строчных русских букв,
между соседними словами - запятая, за последним словом - точка. Вывести в
алфавитном порядке все звонкие согласные буквы, которые входят более чем в одно
слово"""

import re
let_case = {'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'л', 'м', 'н', 'р'}
inp_let = set()  # Множество согласных звонких букв в текущей строке
prev_let = set()  # Множество согласных звонких букв, обнаруженных в предыдущих словах
out_let = set()  # Множество согласных, которые присутствуют более, чем в одном слове
while True:
    print('Enter the words, put comma between them and at the end point:')
    w_inp = input().lower()
    if w_inp.isdigit():
        print('Please input string!\n')
        continue
    else:
        if re.search('[а-я]', w_inp):
            if w_inp.endswith('.'):
                if ',' in w_inp:
                    w_inp = w_inp.split(', ')
                    for i in w_inp:
                        for j in i:
                            if j in let_case:
                                inp_let.add(j)
                                out_let |= inp_let & prev_let
                                prev_let |= inp_let
                                inp_let.clear()
                    if out_let == set():
                        print('None available letters! Try again.\n')
                        continue
                    else:
                        w_out = sorted(out_let)
                        w_str = '; '.join(w_out)
                        print('Voiced consonants letters: ', w_str + '.')
                else:
                    print('You have to put commas between words, or you wri'
                    'te one word!\n')
                    continue
            else:
                print('You have to put point after words!\n')
                continue
        else:
            print('Word should be written in the Russian alphabet!\n')
            continue
    ask = input('\nDo you want continue? [y/n]: ')
    if ask == 'y':
        out_let.clear()
        continue
    else:
        break
