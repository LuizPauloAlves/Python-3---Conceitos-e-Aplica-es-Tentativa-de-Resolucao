import random
G = 'NUMEROS.txt'
arq = open(G,'w')
for i in range(2000):
    n = random.randint(1,100000)
    if i < 2000-1:
        w = str(n) + '\n'
        arq.write(w)
    else:
        w = str(n)
        arq.write(w)