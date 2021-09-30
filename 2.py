A = int(input("a = "))
B = int(input("b = "))
if A < B:
    B += 1
    for i in range(A, B):
        print(i)
else:
    A += 1
    for i in range(B, A)[::-1]:
        print(i)