# Семенов Денис КНІТ 16-А
"""Условие: В основу древнеяпонского календаря был положен 60-летний цикл,
состоящий из пяти 12-летних подциклов. Подциклы обозначались названиями цвета:
зелёный, красный, желтый, белый и черный. Внутри каждого подцикла, годы носили
названия животных: крысы, коровы, тигра, зайца, драковна, змеи, лошади, овцы,
обезьяны, курицы, собаки и свиньи. 1984 год (год зеленой крысы) - начало
очередного цикла. Разработать программу, которая вводит номер некоторого года
нашей эры и печатает его название по древнеяпонскому календарю."""

y_color = ['green', 'red', 'yellow', 'white', 'black']
y_animal = ['rat', 'cow', 'tiger', 'rabbit', 'dragon', 'snake', 'horse',
            'sheep', 'monkey', 'rooster', 'dog', 'pig']

while True:
    try:
        year = int(input('Enter a year of our era: '))
    except ValueError:
        print('Year must be an integer value, try again:)\n')
        continue
    i = 0
    if year >= 0:
        year = (year - 4) % 60
        while year not in range(12):
            year -= 12
            i += 1
        print('Year of', y_color[i], y_animal[year])
    else:
        print('Year must be of our era!')
    ask = input('\nDo you want continue? [y/n]: ')
    if ask == 'y':
        continue
    else:
        break
