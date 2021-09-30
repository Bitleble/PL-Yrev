def fb(f):
    if f == 1:
        return 0
    if f in (2, 3):
        return 1
    return fb(f - 1) + fb(f - 2)

a = []
n = int(input("9 Задание число N = "))
for f in range(1, n + 1):
    v = fb(f)
    a.append(v)
print(sum(a))

print("Задание 10")

n = int(input("Количество чисел из ряда = "))
k = int(input("Порядковый номер в ряду (начало) = "))
a = []
for f in range(k, n + 1):
    c = fb(f)
    a.append(c)
print(sum(a))