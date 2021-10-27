def KolDel(n):
    k = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            k += 1
            if i * i != n:
                k += 1
        i += 1
    return k

n = int(input('N: '))
m = int(input('M: '))
max = 0
a = []
for i in range(n, m + 1):
    kol=KolDel(i)
    if i == n:
      max = KolDel(n)
    if kol > max:
      max = kol
      a = [i]
    elif max == kol:
      a.append(i)
print('Максимальное количество: ',max)
print(a)