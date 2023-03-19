import random

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
       print(lista)
       while esquerda <= direita and lista[esquerda] <= pivot:
           esquerda = esquerda + 1
           print(esquerda+1, lista[esquerda], 'Esquerda', pivot)

       while lista[direita] >= pivot and direita >= esquerda:
           direita = direita -1
           print(direita+1, lista[direita], 'direita', pivot)

       if direita < esquerda:
           feito = True
       else:

           temp = lista[esquerda]
           print(lista[esquerda],esquerda+1,'>',lista[direita],direita+1)
           lista[esquerda] = lista[direita]
           lista[direita] = temp

   temp = lista[primeiro]
   lista[primeiro] = lista[direita]
   lista[direita] = temp


   return direita

lista = [5,4,6,3,7,8,2,1,9]
#for i in range(10):
#    lista.append(random.randint(1,50))
quickSort(lista)
print(lista)