print("Zadanie 1")

a = int(input(" a = "))
b = int(input(" b = "))
if a <= b:
    b += 1
    for i in range(a, b):
        print(i)