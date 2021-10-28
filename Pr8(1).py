import random
def Zmn(A, m1, k1):
    l = A[k1]
    A[k1] = A[m1]
    A[m1] = l



m = int(input('Ввод строки для замены: ')) - 1
n = int(input('Ввод размерности матрицы: '))
a = []
k = 0
for i in range(n):
    b = []
    for i in range(n):
        b.append(random.randint(0, 10))
    a.append(b)
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
max1 = a[0][0]
for i in range(n):
    for j in range(n):
        if i == j and a[i][j] > max1:
                max1 = a[i][j]
                print('Номер строки с макс значением', i+1)
                k = i
if k == m:
    print('Нечего менять ')
    exit(1)

Zmn(a, m, k)
print('Изменённая матрица: ')
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()