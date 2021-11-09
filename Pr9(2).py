n = int(input('Число n:'))
a = [[0] * n for i in range(n)]
st, m = 1, 0
a[n // 2][n // 2] = n * n  # Центр
for i in range(n // 2):
    # Заполнение верхней горизонтальной матрицы
    for j in range(n - m):
        a[i][j + i] = st
        st += 1
    # Заполнение правой вертикальной матрицы
    for j in range(i + 1, n - i):
        a[j][-i - 1] = st
        st += 1
    # Заполнение нижней горизонтальной матрицы
    for j in range(i + 1, n - i):
        a[-i - 1][-j - 1] = st
        st += 1
    # Заполнение левой вертикальной матрицы
    for j in range(i + 1, n - (i + 1)):
        a[-j - 1][i] = st
        st += 1
    m += 2
for i in a:
    print(*i)
with open('viv.txt', 'w') as out:
    out.write('Изменёная матрица:' + '\n')
    for i in a:
        out.write(' '.join([str(a) for a in i]) + '\n')
