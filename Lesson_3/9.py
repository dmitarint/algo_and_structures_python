# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random
#Создаем матрицу
line=9
colmn=9
a=[]
b=[0]*line
for i in range(colmn):
    a.append([])
    for j in range(line):
        a[i].append(random.randint(0,100))
# Печатаем матрицу
for i in range(colmn):
    print(a[i])

# Ищем минимальный элемент в столбце
for i in range(line):
    min=100
    for j in range(colmn):
        if a[j][i]<min:
            min=a[j][i]
        b[i]=min
print ('Min list ', b)

#Ищем максимальный элемент среди минимальных элементов столбцов матрицы
max=0
for i in b:
    if i>max:
        max=i
print('Max ', max)

