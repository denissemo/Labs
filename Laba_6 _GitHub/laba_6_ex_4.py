# Семенов Денис КНІТ 16-А
"""Условие: В основу древнеяпонского календаря был положен 60-летний цикл,
состоящий из пяти 12-летних подциклов. Подциклы обозначались названиями цвета:
зелёный, красный, желтый, белый и черный. Внутри каждого подцикла, годы носили
названия животных: крысы, коровы, тигра, зайца, драковна, змеи, лошади, овцы,
обезьяны, курицы, собаки и свиньи. 1984 год (год зеленой крысы) - начало
очередного цикла. Разработать программу, которая вводит номер некоторого года
нашей эры и печатает его название по древнеяпонскому календарю. """

from enum import Enum
class Y_color(Enum):
    green = 0
    red = 1
    yellow = 2
    white = 3
    black = 4

class Y_animal(Enum):
    monkey = 0
    rooster = 1
    dog = 2
    pig = 3
    rat = 4
    cow = 5
    tiger = 6
    rabbit = 7
    dragon = 8
    snake = 9
    horse = 10
    sheep = 11

while True:
    try:
        year = int(input('Enter a year of our era: '))
    except ValueError:
        print('Year must be an integer value, try again:)\n')
        continue
    i = 0
    if year >= 0:
        year_c = (year - 4) % 60
        while year_c not in range(12):
            year_c -= 12
            i += 1
        animal = year % 12
        print('Year of', Y_color(i).name, Y_animal(animal).name)
    else:
        print('Year must be of our era!')
    ask = input('\nDo you want continue? [y/n]: ')
    if ask == 'y':
        continue
    else:
        break
