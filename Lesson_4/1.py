"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import timeit
import cProfile

#Решение через рекурсию
def f():
    def obr(n,ln):
        s=''
        m=0
        if m==ln: #базовое условие
            return s
        else:
            m+=1
            return s+n[ln-m]+obr(n,ln-m)

    n = '4565435'
    ln=len(n)
    print(obr(n,ln))



# Время выполнения через рекурсию 0.00016164399999999898
# Время выполнения через While 0.00020988099999999857
# Сложность как через рекурсию, так и через While квадратичная О(N**2)


# # Решение через While
# def f():
#     def obr(n):
#         ln = len(n)
#         s = ''
#         m = int()
#         m = 0
#         while m != ln:
#             s = s + str(n[ln-1 - m])
#             m += 1
#         if m == ln:
#             return s
#     n = '4565435'
#     print(obr(n))

# cProfile.run('f()')
print(timeit.timeit("f()",setup='from __main__ import f', number=10))