# Семенов Денис КНІТ 16-А
# Условие: по названию страны 's' определить название её континента
from enum import Enum
class Continent(Enum):
    Asia = 1
    America = 2
    Europe = 3

class Country(Enum):
    Germany = 3
    Cuba = 2
    Laos = 1
    Monaco = 3
    Bangladesh = 1
    Ukraine = 3
while True:
    try:
        user_inp = input('\nВведите название страны на англ. языке: ')
        user_inp = user_inp.capitalize()
        s = Country[user_inp]
        s = s.value
    except KeyError or ValueError:
        print('Такой страны нет в списке, может вы ошиблись, давайте попробуем'
        ' снова:)')
        continue
    print('Континент: ', Continent(s).name)
    ask = input('Хотите продолжить? [y/n]: ')
    if ask == 'y':
        continue
    else:
        break
