# Семенов Денис КНІТ 16-А
# Условие: по названию страны 's' определить название её континента
from enum import Enum
class Continent(Enum):
    Asia = 1
    Europe = 2
    America = 3

class Country(Enum):
    Germany = 1
    Cuba = 2
    Laos = 3
    Monaco = 4
    Bangladesh = 5
    Ukraine = 6

Asia = Country.Bangladesh.name, Country.Laos.name
Europe = Country.Germany.name, Country.Ukraine.name, Country.Monaco.name
America = Country.Cuba.name
while True:
    try:
        user_inp = input('\nВведите название страны на англ. языке: ')
        user_inp = user_inp.capitalize()
        s = Country[user_inp].name
    except KeyError or ValueError:
        print('Такой страны нет в списке, может вы ошиблись, давайте попробуем'
        ' снова:)')
        continue
    for i in Asia:
        if i == s:
            print('Континент: ', Continent.Asia.name)
    for i in Europe:
        if i == s:
            print('Континент: ', Continent.Europe.name)
    if America == s:
        print('Континент: ', Continent.America.name)
    ask = input('Хотите продолжить? [y/n]: ')
    if ask == 'y':
        continue
    else:
        break
