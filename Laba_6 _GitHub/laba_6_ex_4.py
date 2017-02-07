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

start = -57  # Начало отсчета
flag = True
while True:
    try:
        end = int(input('Enter a year of our era: '))
    except ValueError:
        print('Year must be an integer value, try again:)')
        continue
    if end < 0:
        print('Year must be of our era!')

    while flag:
        for i in y_color:
            for j in y_animal:
                start += 1
                if start == end:
                    print('Year of', i, j)
                    flag = False
                    break
    ask = input('Do you want continue? [y/n]: ')
    if ask == 'y':
        start = -57
        flag = True
        continue
    else:
        break
