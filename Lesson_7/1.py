"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random

massive = [random.randint(-100, 100) for _ in range(20)]

def bubble(orig_list):
    j = 1
    while j < len(orig_list):
        check=0
        for i in range(len(orig_list)-j):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
            else:
                check+=1
        if check==len(orig_list)-j:
            # print (orig_list[j:])
            break
        j += 1
    return orig_list


print(bubble(massive))
