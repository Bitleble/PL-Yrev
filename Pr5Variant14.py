v = str(input("Введите строку на русском языке-- "))
v = v.lower()
for s in v.split():
    if (s.startswith("а") or s.endswith("я")):
        print(s)