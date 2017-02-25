# Семенов Денис КНІТ 16-А
"""Условие: дана непустая последовательность слов из строчных русских букв,
между соседними словами - запятая, за последним словом - точка. Вывести в
алфавитном порядке все звонкие согласные буквы, которые входят более чем в одно
слово"""

import re
let_case = {'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'л', 'м', 'н', 'р'}
letters = []
while True:
    print('Enter the words, put comma between them and at the end point:')
    w_inp = input().lower()
    if w_inp.isdigit():
        print('Please input string!')
        continue
    else:
        if re.search('[а-я]', w_inp):
            if w_inp.endswith('.'):
                if ',' in w_inp or (',' not in w_inp and w_inp.endswith('.')
                                    and ' ' not in w_inp):
                    w_inp = w_inp.split(', ')
                    for i in w_inp:
                        for j in i:
                            if j in let_case:
                                letters.append(j)
                    for c in letters:
                        if letters.count(c) == 2:
                            pass
                        else:
                            letters.remove(c)
                            print('None available letters')
                else:
                    print('You have to put commas between words!')
                    continue
            else:
                print('You have to put point after words!')
                continue

        else:
            print('Word should be written in the Russian alphabet!')
            continue
    letters = set(letters)
    w = sorted(letters)
    w_str = '; '.join(w)
    print('Voiced consonants letters: ', w_str)
    ask = input('Do you want continue? [y/n]: ')
    if ask == 'y':
        continue
    else:
        break
