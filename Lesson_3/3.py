#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

import random
# Создаем массив со случайными числами от-100 до 100
a=[random.randint(-100,100) for i in range(20)]
print(a)
min=100
max=-101
indexmin=0
indexmax=0
for i in range(20):
    if a[i]<min: #Цикл для поиска минимального числа
        min=a[i]
        indexmin=i
    if a[i]>max: #Цикл для поиска максимальноо числа
        max=a[i]
        indexmax=i
#Замена max и min местами
a[indexmin],a[indexmax]=a[indexmax],a[indexmin]
print(a)