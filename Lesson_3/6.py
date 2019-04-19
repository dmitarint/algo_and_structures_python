"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random
# Создаем массив со случайными числами от-100 до 100
a=[random.randint(-100,100) for i in range(20)]
print(a)
min=100
max=-100

#Циклом вычисляем минимальное и максимальное число число и их индекс
for i in range(20):
    if a[i]<min:
        min=a[i]
        positionmin=i
        print(f'Мин: индекс {positionmin}  значение {min}')
    elif a[i]>max:
        max=a[i]
        positionmax=i
        print(f'Макс: индекс {positionmax}  значение {max}')
#Провкеряем расположение индексов максимального и минимального числа и вычисляем сумму между жлементами
if positionmax>positionmin:
    print(sum(a[positionmin+1:positionmax]))
else:
    print(sum(a[positionmax+1:positionmin]))