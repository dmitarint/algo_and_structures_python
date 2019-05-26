"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

import random

m = random.randint(30, 70)
massive = [random.randint(-500, 500) for _ in range(2 * m + 1)]


# print(massive)

def sort(listr):
    left = 0
    right = len(listr) - 1
    while left <= right:
        for i in range(left, right):
            if listr[i] > listr[i + 1]:
                listr[i], listr[i + 1] = listr[i + 1], listr[i]
        right -= 1
        for i in range(right, left, -1):
            if listr[i] < listr[i - 1]:
                listr[i], listr[i - 1] = listr[i - 1], listr[i]
        left+=1
    return listr
n=sort(massive)
print(n)
print('Медиана ', n[m])