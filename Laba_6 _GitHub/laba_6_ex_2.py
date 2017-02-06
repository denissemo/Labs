from enum import Enum
class Measure(Enum):
    decimetre = 1
    kilometre = 2
    metre = 3
    millimetre = 4
    centimetre = 5
while True:
    try:
        inp_len = float(input('Введите длину: '))
        inp_value = Measure[input('Введите величину на англ. языке: ')]
    except (ValueError, KeyError):
        print('Такого значения нету, может вы ошиблись, попробуйте снова')
        continue
    if inp_value == Measure.decimetre:
        print(inp_len * 0.1, 'метров', sep=' - ')
    elif inp_value == Measure.kilometre:
        print(inp_len * 1000, 'метров', sep=' - ')
    elif inp_value == Measure.metre:
        print(inp_len, 'метров', sep=' - ')
    elif inp_value == Measure.millimetre:
        print(inp_len * 0.001, 'метров', sep=' - ')
    elif inp_value == Measure.centimetre:
        print(inp_len * 0.01, 'метров', sep=' - ')
    ask = input('Хотите продолжить? [y/n]: ')
    if ask == 'y':
        continue
    else:
        break
