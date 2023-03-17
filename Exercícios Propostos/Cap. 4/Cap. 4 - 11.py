import random
N = int(input('+5000:'))
NV = []
while N <= 5000:
    N = int(input('+5000:'))
for i in range(N):
    NV.append(random.randint(1,100))
x = 1
while x > 0:
    x = int(input('Valor qualquer:'))
    a = 0
    for i in range(N):
        if x == NV[i] and a == 0:
            print("O valor {} esta na posição {}".format(x, i),end="")
            a = 1
        elif x == NV[i] and a != 0:
            print(", {}".format(i),end="")
            a += 1
    if a > 0:
        print("\nO numero {} foi encontrado {} vezes".format(x, a))
    else:
        print("não foi encontrado este numero")