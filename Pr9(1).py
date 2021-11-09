import random


def Zmn(A, m1, k1):
    l = A[k1]
    A[k1] = A[m1]
    A[m1] = l


def zap(file1):
    for x in range((n ** 2)+1):
        p = random.randint(-10, 10)
        file1.write(str(p) + '\n')


file = open('pr.txt', 'r')
file01 = open('pr.txt', 'w')
out = open('viv1.txt', 'w')
m = int(input('Ввод строки для замены: ')) - 1
n = (int(input('Введите ширину/высоту матрицы: ')))
zap(file01)
file01.close()
a = []
a1 = []
for line in file:
    for i in range(n):
        a1 = []
        for j in range(n):
            a1.append([int(x) for x in file.readline().split()])
        a.append(a1)
file.close()
for i in range(n):
    for j in range(n):
        print(*(a[i][j]), '', end='')
    print()
k = 0
max1 = a[0][0]
for i in range(n):
    for j in range(n):
        if i == j and a[i][j] > max1:
            max1 = a[i][j]
            print('Номер строки с макс значением', i + 1)
            k = i

if k == m:
    print('Нечего менять ')
    if k == m:
        out.write('Нечего менять.')
        exit(1)

Zmn(a, m, k)
print('Изменённая матрица: ')
for i in range(n):
    for j in range(n):
        print(*(a[i][j]), end=' ')
    print()
    out.write('Изменёная матрица:' + '\n')
for i in a:
    out.write(' '.join([str(a) for a in i]) + '\n')
out.close()