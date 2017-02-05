# Семенов Денис КНІТ 16-А
def next_month(m):
    """Функция меняет месяц на следующий,\
     если введен 31 день месяца"""
    if m < 12:
        m += 1
    else:
        m = 1
    return m


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
            year = int(input('Введите год [1901, 2015]: '))
        except ValueError:
            print('Введите целое число!')
            continue
        if year not in range(1901, 2016):
            print('Введите допустимое значение!')
            continue
        break
    day += 1
    if day > 31:
        day = 1
        month = next_month(month)
        year += 1
    print('Дата следующего дня: {}.{}.{}'.format(day, month, year))
    ask = input('Хотите продолжить? [y/n]: ')
    if ask == 'y':
        continue
    else:
        break
