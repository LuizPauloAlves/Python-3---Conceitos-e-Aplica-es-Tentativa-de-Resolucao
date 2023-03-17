a = int(input('Tamanho da lista: '))
N, R = [], []
i = 0
while i < a:
    N.append(input("digite o valor {} de {}: ".format(i+1, a)))
    i += 1
i = a - 1
print(N)
N.reverse()
while i >= 0:
    #print(N)
    j = i - 1
    while j >= 0:
        #print(j, i)
        if N[i] == N [j]:
            #print(i,j)
            #print(N)
            R.append(N[i])
            N.remove(N[i])
            i -= 1
        j -=1
    i -= 1
N.reverse()
print(N,R)