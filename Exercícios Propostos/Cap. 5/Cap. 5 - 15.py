import random
import time
def cresente(L):
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i] < L[j]:
                aux = L[i]
                L[i] = L[j]
                L[j] = aux
    return L

def quickSort(lista):
   quickSort2(lista,0,len(lista)-1)

def quickSort2(lista,primeiro,ultimo):
   if primeiro<ultimo:

       splitpoint = partition(lista,primeiro,ultimo)

       quickSort2(lista,primeiro,splitpoint-1)
       quickSort2(lista,splitpoint+1,ultimo)


def partition(lista,primeiro,ultimo):
   pivot = lista[primeiro]

   esquerda = primeiro+1
   direita = ultimo

   feito = False
   while not feito:
       while esquerda <= direita and lista[esquerda] <= pivot:
           esquerda = esquerda + 1

       while lista[direita] >= pivot and direita >= esquerda:
           direita = direita -1

       if direita < esquerda:
           feito = True
       else:

           temp = lista[esquerda]
           lista[esquerda] = lista[direita]
           lista[direita] = temp

   temp = lista[primeiro]
   lista[primeiro] = lista[direita]
   lista[direita] = temp


   return direita

lista,lista1, lista2 = [],[],[]
for i in range(10000):
    lista.append(random.randint(1,50))
lista1 = lista
inicio = time.time()
quickSort(lista1)
#print(lista1,'Lista 1')
fim = time.time()
print(fim - inicio)

lista2 = lista
inicio = time.time()
cresente(lista2)
#print(lista2,'Lista 2')
fim = time.time()
print(fim - inicio)
