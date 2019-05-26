"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
n=40 #номер по счету простого числа
a=[0]*n**2
for i in range(n**2):
    a[i]=i

print (a)
b=[1,2]
m=2
for i in range(2,n**2):
    for j in range(1,n**2):
        if a[i]%a[j]!=0 and i!=j:
            b.append(i)
print (b)
print(b[n])

# # Решето Эратосфена
# n=40 #номер по счету простого числа
# a=[0]*n**2
# for i in range(n**2):
#     a[i]=i
# a[1]=0
# m=2
# while m<n:
#     if a[m]!=0:
#         j=m*2
#         while j<n:
#             a[j]=0
#             j=j+m
#     m+=1
# # print (a)
# b=[]
# for i in a:
#     if a[i]!=0:
#         b.append(a[i])
# del a
# print (len(b))
# print(b[n])
