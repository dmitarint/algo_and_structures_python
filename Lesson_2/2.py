"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

n=str(input('Введите натуральное число:'))
even=[]
odd=[]
for i in n:
    if int(i)%2==0:
        even.append(i)
    else:
        odd.append(i)
print('Четные числа: ', even)
print('Нечетные числа: ', odd)
