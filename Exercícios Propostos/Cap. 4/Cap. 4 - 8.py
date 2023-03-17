import random
i = 0
V = []
while i == 0:
    N = int(input("Digite um valor entre 0 a 50: "))
    if 50 >= N >= 0:
        i = 1
while  i <= N:
    V.append(random.randint(1,50))
    i += 1
print(V)
X = 1
while X != 0 and N != 0:
    i = 0
    X = int(input('Digite um valor: '))
    while i < N:
        if V[i] == X:
            V.remove(X)
            i -= 1
            N -= 1
        i += 1