# Семенов Денис КНІТ 16-А
# Условие: по заданой дате, определить дату следующего дня

while True:
    while True:
        try:
            day = int(input('Введите день: '))
        except ValueError:
            print('Введите целое число!')
            continue
        if day not in range(1, 32):
            print('Введите допустимое значение!')
            continue
        break
    while True:
        try:
            month = int(input('Введите месяц: '))
        except ValueError:
            print('Введите целое число!')
            continue
        if month not in range(1, 13):
            print('Введите допустимое значение!')
            continue
        break
    while True:
        try:
            year = int(input('Введите год [1901, 2017]: '))
        except ValueError:
            print('Введите целое число!')
            continue
        if year not in range(1901, 2018):
            print('Введите допустимое значение!')
            continue
        break
    day += 1
    if day not in range(32):
        day = 1
        if month in range(12):
            month += 1
        else:
            month = 1
            year += 1
    print('Дата следующего дня: {}.{}.{}'.format(day, month, year))
    ask = input('Хотите продолжить? [y/n]: ')
    if ask == 'y':
        continue
    else:
        break
