# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

# координата задается черех список
m1 = []
m1.append(int(input("Введите координату x1: ")))
m1.append(int(input("Введите координату y1: ")))
m2 = []
m2.append(int(input("Введите координату x2: ")))
m2.append(int(input("Введите координату y2: ")))

k = (m1[1] - m2[1]) / (m1[0] - m2[0])
b = m1[1] - k * m2[1]

print(" y = %d*x + %d" % (k, b))
