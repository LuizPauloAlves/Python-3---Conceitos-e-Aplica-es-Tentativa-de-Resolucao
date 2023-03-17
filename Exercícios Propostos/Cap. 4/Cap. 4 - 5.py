n1 = int(input("Tamanho da lista 1 > "))
n2 = int(input("Tamanho da lista 2 > "))
lista1, lista2, lista3 = [], [], []
numero, i = 1 , 1
lista1.append(int(input("digite o valor para a posição {} da Lista 1>".format(numero))))
while i < n1:
    numero = int(input("digite o valor para a posição {} da Lista 1>".format(i+1)))
    conf, j = 0, 0
    while j < i and conf == 0:
        if conf == 0 and lista1[j] == numero:
            conf = 1
        j += 1
    if conf == 0:
        lista1.append(numero)
        i += 1
print(lista1)
numero, i = 1 , 1
lista2.append(int(input("digite o valor para a posição {} da Lista 2>".format(numero))))
while i < n2:
    numero = int(input("digite o valor para a posição {} da Lista 2>".format(i+1)))
    conf, j = 0, 0
    while j < i and conf == 0:
        if conf == 0 and lista2[j] == numero:
            conf = 1
        j += 1
    if conf == 0:
        lista2.append(numero)
        i += 1
print(lista2)
numero, i= 0 , 1
lista3.append(lista1[0])
while i < (n1+n2):
    if i < n1:
        numero = lista1[i]
    elif i >= n1:
        numero = lista2[i-n1]
    conf, j = 0, 0
    while j < len(lista3) and conf == 0:
        print(j, lista3[j], numero)
        if conf == 0 and lista3[j] == numero:
            conf = 1
            print(conf)
        j += 1
    if conf == 0:
        lista3.append(numero)
    i += 1
print(lista3)