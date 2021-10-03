A1 = int(input(" a = "))
B1 = int(input(" b = "))
for i in range(B1, A1 + 1)[::-1]:
    if i % 2 == 0:
        continue
    print(i)