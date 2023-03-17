from random import randint
r1 = randint(1,10)   #criar um valor aleatorio entre 1 a 10
r2 = randint(1,10)
i = 0
a, b = [], []   #criar dois vetores vazios a e b usando []
while i < r1:   #while para criar o vetor com tamanho aleatorio
    a.append(randint(0,50))   #valor aleatorio para as posições do velor em relação com i
    i +=1
i = 0
while i < r2:
    b.append(randint(0,50))
    i +=1
c = a+b   #concatenação dos vetores a e b
print(c)