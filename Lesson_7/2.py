"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

import random

massive = [random.random() * 50 for _ in range(100)]


# print(massive)

def sort(listr):
    if len(listr) > 1:
        center = len(listr) // 2
        left = listr[:center]
        right = listr[center:]
        sort(left)
        sort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                listr[k] = left[i]
                i += 1
            else:
                listr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            listr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            listr[k] = right[j]
            j += 1
            k += 1
        return listr

print(massive)
print(sort(massive))
