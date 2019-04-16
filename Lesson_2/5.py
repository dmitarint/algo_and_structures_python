"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

# Задаем рекурсию на вывод символов в строке по 10 пар
def des(i, n):
    if n == 0:
        return ''
    else:
        return str(i) + ' ' + str(chr(i) + ' ' + des(i + 1, n - 1))

#Задаем цикл от 32 до 127 с шагом 10. Проводится проверка условий на последний шаг
for i in range(32, 127, 10):
    if 127 - i > 10:
        print(des(i, 10))
    else:
        print(des(i, 127 - i))


