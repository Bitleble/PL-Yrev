n = int(input("Число n = "))

for i in range(n):
    for j in range(1, i + 2):
        print(j, end='')
    print()