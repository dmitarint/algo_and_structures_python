"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import defaultdict
import functools
numbers = defaultdict()
a = input('введите 1-е число: ')
b = input('введите 2-е число: ')
numbers[f'a {a}'] = list(a)
numbers[f'b {b}'] = list(b)
for i, c in numbers.items():
    print(i, c)
# Сложение:
summa = sum(int(''.join(i), 16) for i in numbers.values())
print('сумма равна: ', list('%x' % summa))
# Умножение:
mult = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in numbers.values()])
print("Произведение: ", list('%X' % mult))

