n = int(input("Quantos termos da PG:"))
r = int(input("Razão da PG:"))
p1 = int(input("Primeiro termo da PG:"))
i = 0
print(p1)
while i < (n-1):
    p1 *= r
    print(p1)
    i += 1