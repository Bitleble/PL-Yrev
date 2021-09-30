N = int(input("Число n = "))
f = 1
while N > 1:
    f *= N
    N -= 1
print(f)