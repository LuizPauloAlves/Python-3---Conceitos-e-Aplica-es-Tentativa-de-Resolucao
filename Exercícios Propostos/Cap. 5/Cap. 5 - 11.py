import random
def cresente(L):
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i] < L[j]:
                aux = L[i]
                L[i] = L[j]
                L[j] = aux
    return L

def decresente(L):
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i] > L[j]:
                aux = L[i]
                L[i] = L[j]
                L[j] = aux
    return L
ListaC = []
ListaD = []
for a in range(10):
    ListaC.append(random.randint(0,10))
    ListaD.append(random.randint(0,10))
print(ListaC)
cresente(ListaC)
print(ListaC,'\n',ListaD)
decresente(ListaD)
print(ListaD)
