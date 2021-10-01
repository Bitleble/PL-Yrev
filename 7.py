
n = int(input("Ввод числа n - "))
cur = 1
pr = 1
s = 0
for i in range(1, n + 1):
    cur = pr * i
    s += cur
    pr = cur
print(s)