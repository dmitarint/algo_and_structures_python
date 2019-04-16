"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""
#Решение через рекурсию
def obr(n,ln):
    s=''
    m=0
    if m==ln: #базовое условие
        return s
    else:
        m+=1
        return s+n[ln-m]+obr(n,ln-m)

n = input('введите число: ')
ln=len(n)
print(obr(n,ln))

# Решение через While
def obr(n):
    ln = len(n)
    s = ''
    m = int()
    m = 0
    while m != ln:
        s = s + str(n[ln-1 - m])
        m += 1
    if m == ln:
        return s
n = input('введите число: ')
# print(obr(n))

