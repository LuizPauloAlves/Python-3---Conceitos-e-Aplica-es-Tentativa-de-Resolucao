def repeticao(L, N):
    a = 0
    for i in range(len(L)):
        if N == L[i]:
            a+= 1
    if a == 0:
        return 0
    else:
        return a

L = []
i=0
L.append(int(input("Valor:")))
while L[i] != 0:
    L.append(int(input("Valor:")))
    i+=1
L.pop()
N = int(input("Repeticao:"))
X = repeticao(L, N)
print(X)