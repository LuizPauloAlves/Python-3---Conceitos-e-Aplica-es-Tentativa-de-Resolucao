a = set(input("Fruta A:"))
b = set(input(("Fruta B:")))
print(a|b)
print(a^b)
print(a&b)
if len(a) > len(b):
    print(a - b)
else:
    print(b - a)


