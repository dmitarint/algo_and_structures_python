"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
import random

l = random.randint(0, 100)
for i in range(0, 10):
    a = int(input('Введите число отгадку: '))
    if a == l:
        print('Вы угадали, ваше число ', l)
        exit()
    elif a < l:
        print('ваше число меньше')
    elif a > l:
        print('ваше число больше')
print('К сожалению вы не угадали число')
