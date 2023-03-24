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

arq = open('NUMEROS.txt','r')
text = arq.readlines()
arq.close()
textNew = []
for text in text:
    textNew.append(int(text.rstrip('\n')))
quickSort(textNew)
arq = open('ORDENADOS2.txt','w')
for i in textNew:
    if i != textNew[-1]:
        x = str(i) + '\n'
        arq.write(x)
    else:
        x = str(i)
        arq.write(x)
arq.close()