# Программа меняет максимальное и минимальное число в массиве местами
a = []
for i in range(1, 6):
    a.append(int(input(i)))
k = min(a)
m = max(a)
k1 = a.index(k, 0, 5)
m1 = a.index(m, 0, 5)
l = a[m1]
a[m1] = a[k1]
a[k1] = l
print(k1 + 1, m1 + 1)
print(a)
