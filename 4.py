N = int(input("Ввод кол-ва цифр = "))
a = []
for i in range(1, N + 1):
    v = int(input(i))
    a.append(v)
print("sum =", (sum(a)))