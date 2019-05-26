"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
# plant = dict()
# n = int(input('Введите количество придприятий: '))
# prib = 0
# for i in range(n):
#     name = input('Введите имя предприятия: ')
#     ann = int(input('Введите прибыль за 4 квартала: '))
#     plant[name] = ann
#     prib += ann
# # print(plant)
# # print(prib)
# sred = int(prib / n)
# print('Средняя прибыль ', sred)
# print('Прибыль выше среднего у следующих предприятий: ')
# for i in plant:
#     if plant[i]>sred:
#         print(i)

from collections import namedtuple

n = int(input('введите количество предприятий: '))
companies = namedtuple('company', 'name kvart1 kvart2 kvart3 kvart4')
baza = dict()
for i in range(n):
    company = companies(name=input('Введите имя компании: '),
                        kvart1=int(input('Введите доход компании за 1-й квартал: ')),
                        kvart2=int(input('Введите доход компании за 2-й квартал: ')),
                        kvart3=int(input('Введите доход компании за 3-й квартал: ')),
                        kvart4=int(input('Введите доход компании за 4-й квартал: ')))
    baza[company.name] = (company.kvart1 + company.kvart2 + company.kvart3 + company.kvart4) / 4

count = 0
amount = 0
for zn in baza.values():
    amount += zn
    count += 1
amount = amount / count
print('Средняя прибыль ', amount)
for a, b in baza.items():
    if b >= amount:
        print(f'у компании {a} прибыль {b} выше среднего значения')
for a, b in baza.items():
    if b <= amount:
        print(f'у компании {a} прибыль {b} ниже среднего значения')


