N = int(input("Numero 1 até 30:"))
while N > 30 or N < 1:
    N = int(input("Numero 1 até 30:"))

A, B = set(), set()

for i in range(N):
    A.add(i)

for i in range(30-N):
    B.add(i)

print(A, B)