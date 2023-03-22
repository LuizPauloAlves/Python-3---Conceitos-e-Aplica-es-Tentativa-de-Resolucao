def cresente(L):
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i] < L[j]:
                aux = L[i]
                L[i] = L[j]
                L[j] = aux

arq = open('NUMEROS.txt','r')
text = arq.readlines()
arq.close()
textNew = []
for text in text:
    textNew.append(int(text.rstrip('\n')))
cresente(textNew)
arq = open('ORDENADOS.txt','w')
for i in textNew:
    if i != textNew[-1]:
        x = str(i) + '\n'
        arq.write(x)
    else:
        x = str(i)
        arq.write(x)

