import math
number = float(input('Введите положительное число, большее 2'))
if number <= 2:
    print('Число должно быть больше 2!')
else:
    while number >=2:
        number = math.sqrt(number)
        print(f"{number:.3f}")
